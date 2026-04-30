from fastapi import FastAPI
from models import Book
from fastapi import HTTPException

app = FastAPI()

db = []

@app.post("/books")
def create_book(book: Book):
    for existing_book in db:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    db.append(book)
    return book

@app.get("/books")
def get_all_books():
    return db

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in db:
        if book.id == book_id:
            return book 
     
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/")
def read_root():
    return {"message": "API is running"}
