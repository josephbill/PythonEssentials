from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import author_book_association

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = relationship("Author", secondary=author_book_association, back_populates="books")

    def __init__(self, title):
        self.title = title

    def add_author(self, author):
        self.authors.append(author)

    def __str__(self):
        return f"Book(id={self.id}, title={self.title})"
