from sqlalchemy.orm import Session
from models import Product

def create_product(db: Session, data):
    new = Product(**data)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def list_products(db: Session, search: str | None, skip: int, limit: int):
    q = db.query(Product)
    if search:
        q = q.filter(Product.name.contains(search))
    return q.offset(skip).limit(limit).all()

def get_product(db: Session, pid: int):
    return db.query(Product).filter(Product.id == pid).first()
