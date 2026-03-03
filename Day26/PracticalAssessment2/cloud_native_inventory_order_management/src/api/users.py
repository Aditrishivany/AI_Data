from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.db.models import User
from src.dependencies import get_db
from src.security import hash_password
from src.schemas import UserCreate, UserOut, UserUpdate
from src.services.activity_logger import log_activity

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.id.desc()).all()


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    user_data = payload.model_dump(exclude={"password"})
    if payload.password:
        user_data["password_hash"] = hash_password(payload.password)

    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)

    await log_activity("CREATE", "USER", f"Created user: {user.email}")
    return user


@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    await log_activity("UPDATE", "USER", f"Updated user id: {user.id}")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(user)
    db.commit()
    await log_activity("DELETE", "USER", f"Deleted user id: {user_id}")
