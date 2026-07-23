from sqlmodel import create_engine


sqlite_file_name = "book.db"

engine = create_engine(
    f"sqlite:///{sqlite_file_name}",
    echo=True
)