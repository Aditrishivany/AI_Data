from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    likes = Column(Integer, default=0)

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    text = Column(String)
