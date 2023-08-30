from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import author_book_association

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary=author_book_association, back_populates="authors")

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Author(id={self.id}, name={self.name})"
