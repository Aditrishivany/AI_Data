from sqlalchemy.orm import Session
from models import Comment

def add_comment(db: Session, data):
    comment = Comment(**data)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment
