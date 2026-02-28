from sqlalchemy.orm import Session
from models import Blog

def create_blog(db: Session, data):
    blog = Blog(**data)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def like_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        blog.likes += 1
        db.commit()
    return blog
