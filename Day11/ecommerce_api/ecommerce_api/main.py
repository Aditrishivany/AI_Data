from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine
from schemas import *
from auth import get_db
from user_crud import create_user, login_user
from product_crud import create_product, list_products, get_product
from blog_crud import create_blog, like_blog
from comment_crud import add_comment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Balanced E-Commerce API")


# -------------------------
# USER AUTH
# -------------------------
@app.post("/register")
def register(user: UserCreate, db=Depends(get_db)):
    return create_user(db, user.username, user.password)

@app.post("/login")
def login(user: UserCreate, db=Depends(get_db)):
    token = login_user(db, user.username, user.password)
    if not token:
        raise HTTPException(401, "Invalid credentials")
    return {"access_token": token}


# -------------------------
# PRODUCTS
# -------------------------
@app.post("/products")
def add_product(p: ProductBase, db=Depends(get_db)):
    return create_product(db, p.model_dump())

@app.get("/products")
def get_products(search: str | None = None, skip: int = 0, limit: int = 10, db=Depends(get_db)):
    return list_products(db, search, skip, limit)

@app.get("/products/{pid}")
def product_detail(pid: int, db=Depends(get_db)):
    product = get_product(db, pid)
    if not product:
        raise HTTPException(404, "Product not found")
    return product


# -------------------------
# BLOG POSTS
# -------------------------
@app.post("/blogs")
def create_blog_post(b: BlogCreate, db=Depends(get_db)):
    return create_blog(db, b.model_dump())

@app.post("/blogs/{bid}/like")
def like(bid: int, db=Depends(get_db)):
    blog = like_blog(db, bid)
    if not blog:
        raise HTTPException(404, "Blog not found")
    return blog


# -------------------------
# COMMENTS
# -------------------------
@app.post("/comments")
def add_comment_route(c: CommentCreate, db=Depends(get_db)):
    return add_comment(db, c.model_dump())
