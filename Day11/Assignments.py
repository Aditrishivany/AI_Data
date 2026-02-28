# ============================================================
# ASSIGNMENT 1: HELLO REST (GET /)
# ============================================================

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# Fake In-Memory Database (shared by all assignments)
books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki"},
    {"id": 3, "title": "The Psychology of Money", "author": "Morgan Housel"},
]


@app.get("/")
def hello_rest():
    return {"message": "Welcome to REST API"}




# ============================================================
# ASSIGNMENT 2: SIMPLE RESOURCE (GET /books)
# ============================================================

@app.get("/books")
def get_all_books():
    return books



# ============================================================
# ASSIGNMENT 3: PATH PARAMETER (GET /books/{book_id})
# ============================================================

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")




# ============================================================
# ASSIGNMENT 4: CREATE RESOURCE (POST /books)
# ============================================================

class BookIn(BaseModel):
    title: str = Field(min_length=3)
    author: str

class BookOut(BaseModel):
    id: int
    title: str
    author: str


@app.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookIn):
    new_id = len(books) + 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book




# ============================================================
# ASSIGNMENT 5: UPDATE RESOURCE (PUT /books/{book_id})
# ============================================================

class BookUpdate(BaseModel):
    title: str = Field(min_length=3)
    author: str

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookUpdate):
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            updated_book = {"id": book_id, **book.model_dump()}
            books[index] = updated_book
            return updated_book

    raise HTTPException(status_code=404, detail="Book not found")




# ============================================================
# ASSIGNMENT 6: DELETE RESOURCE (DELETE /books/{book_id})
# ============================================================

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")




# ============================================================
# ASSIGNMENT 7: QUERY PARAMETERS (GET /books?author=...)
# ============================================================

@app.get("/filter-books")
def filter_books(author: str | None = None):
    if author:
        return [
            book for book in books
            if author.lower() in book["author"].lower()
        ]
    return books




# ============================================================
# ASSIGNMENT 8: STATUS CODES & VALIDATION (Title >= 3 chars)
# ============================================================

class ValidateBook(BaseModel):
    title: str = Field(min_length=3)
    author: str

@app.post("/validate-book", status_code=status.HTTP_201_CREATED)
def validate_book(book: ValidateBook):
    # Pydantic already ensures title >= 3 chars
    return {"message": "Book is valid", "data": book}
