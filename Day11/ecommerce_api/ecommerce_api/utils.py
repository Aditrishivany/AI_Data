from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

SECRET = "SECRET_KEY"
ALGO = "HS256"

pwd = CryptContext(schemes=["bcrypt"])

def hash_pass(password: str):
    return pwd.hash(password)

def verify_pass(password, hashed):
    return pwd.verify(password, hashed)

def create_token(data: dict):
    exp = datetime.utcnow() + timedelta(hours=6)
    data.update({"exp": exp})
    return jwt.encode(data, SECRET, algorithm=ALGO)
