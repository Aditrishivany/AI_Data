from pydantic import BaseModel

# USER
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

# PRODUCT
class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductOut(ProductBase):
    id: int

# BLOG
class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    likes: int

# COMMENT
class CommentCreate(BaseModel):
    blog_id: int
    text: str
