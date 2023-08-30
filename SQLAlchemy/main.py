from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.author import Author
from models.book import Book
from models.base import Base

DATABASE_URI = "sqlite:///library.db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)  # Create tables

# Create authors and books
author_name = "J.K. Rowling"
author_name2 = "Joseph Rowling"
book_title = "Harry Potter and the Sorcerer's Stone"
book_title2 = "Second Book"

author1 = session.query(Author).filter_by(name=author_name).first()
if not author1:
    author1 = Author(name=author_name)

book1 = session.query(Book).filter_by(title=book_title).first()
if not book1:
    book1 = Book(title=book_title)

book2 = session.query(Book).filter_by(title=book_title2).first()
if not book2:
    book2 = Book(title=book_title2)

book1.add_author(author1)
book2.add_author(author1)

# ... Similarly, check and add authors and books as needed ...

# Add objects to the session
if author1 not in session:
    session.add(author1)
if book1 not in session:
    session.add(book1)
if book2 not in session:
   session.add(book2)

session.commit()

# Read data
all_authors = session.query(Author).all()
for author in all_authors:
    print("Author:", author.name)
    for book in author.books:
        print(" - Book:", book.title)

# Update data
author_to_update = session.query(Author).filter_by(name=author_name).first()
if author_to_update:
    author_to_update.name = "Joanne Rowling"
    session.commit()

# Delete data
author_to_delete = session.query(Author).filter_by(name="George Orwell").first()

if author_to_delete:
    session.delete(author_to_delete)
    session.commit()
else:
    print("Author not found, unable to delete.")

# Close the session
session.close()
