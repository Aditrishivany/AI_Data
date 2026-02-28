from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.db.models import User
from src.dependencies import get_db
from src.schemas import AuthLogin, AuthRegister, AuthResponse
from src.security import hash_password, verify_password
from src.services.activity_logger import log_activity

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register_user(payload: AuthRegister, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    await log_activity("REGISTER", "AUTH", f"New user registered: {user.email}")
    return AuthResponse(message="Registration successful", user_id=user.id, email=user.email)


@router.post("/login", response_model=AuthResponse)
async def login_user(payload: AuthLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not user.password_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    await log_activity("LOGIN", "AUTH", f"User logged in: {user.email}")
    return AuthResponse(message="Login successful", user_id=user.id, email=user.email)
