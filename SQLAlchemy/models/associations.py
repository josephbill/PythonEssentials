from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

author_book_association = Table(
    'author_book_association',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)
