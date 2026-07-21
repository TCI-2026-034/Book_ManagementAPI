from fastapi import FastAPI, HTTPException, status
from models import Book

app = FastAPI()

books = []

@app.get("/")
def home():
    return {"message": "Book API Running"}

@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }

@app.get("/books")
def get_books():
    return books
@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):

        if book.id == book_id:
            books[index] = updated_book

            return {
                "message": "Book updated successfully",
                "book": updated_book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:
        if book.id == book_id:
            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )