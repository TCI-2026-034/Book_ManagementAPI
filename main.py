from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select

from models import Book


app = FastAPI()


# database connection
sqlite_file_name = "book.db"

engine = create_engine(
    f"sqlite:///{sqlite_file_name}",
    echo=True
)

#create database table
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()



#home route
@app.get("/")
def home():
    return {"message": "Book API Running"}



#create book
@app.post("/books")
def add_book(book: Book):

    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)

        return book



#get all books
@app.get("/books")
def get_books():

    with Session(engine) as session:
        books = session.exec(select(Book)).all()

        return books



#get books by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):

    with Session(engine) as session:

        book = session.get(Book, book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        return book



#update book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    with Session(engine) as session:

        book = session.get(Book, book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        book.title = updated_book.title
        book.author = updated_book.author
        book.price = updated_book.price

        session.add(book)
        session.commit()
        session.refresh(book)

        return book


#delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    with Session(engine) as session:

        book = session.get(Book, book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        session.delete(book)
        session.commit()

        return {
            "message": "Book deleted successfully"
        }