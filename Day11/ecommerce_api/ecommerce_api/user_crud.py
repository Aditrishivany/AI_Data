from sqlalchemy.orm import Session
from models import User
from utils import hash_pass, verify_pass, create_token

def create_user(db: Session, username: str, password: str):
    user = User(username=username, password=hash_pass(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_pass(password, user.password):
        return None
    return create_token({"user_id": user.id})
