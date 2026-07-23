# BookAPI
BookAPI is build using FastAPI that allows users to manage books. This project is created to practice the basics of API development, CRUD operations, request handling, and data validation using Pydantic.

## Features
* Add a new book
* View all books
* View a single book by ID
* Update book details
* Delete a book
* Validate incoming data using Pydantic models
* Handle errors using HTTP exceptions

## Technologies Used
* Python
* FastAPI
* Pydantic
* Uvicorn

## How to Run the Project
1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder:
```bash
cd BookAPI
```

3. Create a virtual environment:
```bash
python -m venv venv
```

4. Activate the virtual environment:
Windows:

```bash
venv\Scripts\activate
```

5. Install the required packages:
```bash
pip install -r requirements.txt
```

6. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

7. Open the API documentation in your browser:
```
http://127.0.0.1:8000/docs
```

## API Endpoints
### Get all books

**GET**
```
/books
```
Returns the list of all available books.

### Get a book by ID
**GET**
```
/books/{id}
```

Returns details of a specific book using its ID.
---

### Add a new book
**POST**
```
/books
```

Adds a new book to the collection.
Example request:
```json
{
  "id": 1,
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20.5
}
```

### Update a book
**PUT**
```
/books/{id}
```
Updates the information of an existing book.

### Delete a book
**DELETE**
```
/books/{id}
```
Removes a book from the collection.

## Project Structure
```
BookAPI/
│
├── main.py        # FastAPI application and API routes
├── models.py      # Pydantic models for data validation
├── requirements.txt
├── README.md
└── venv/
```

## This Is What I Learned
While building this project, I learned how APIs work, how FastAPI handles requests and responses, how CRUD operations are implemented, and how Pydantic helps validate data before processing it.
This project helped me understand the basic workflow of backend development and prepared me for working with databases and more advanced API features.
