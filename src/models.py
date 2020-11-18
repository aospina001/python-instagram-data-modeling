import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False)
    FirstName = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    PostID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('user.UserID'))
    Description = Column(String(500), nullable=False)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'like'
    UserID = Column(Integer, ForeignKey('user.UserID'))
    PostID = Column(Integer, primary_key=True)
    CommentID = Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = 'comment'
    CommentID = Column(Integer, primary_key=True)
    Comment_content = Column(String(500), nullable=False)
    UserID = Column(Integer, ForeignKey('user.UserID'))
    PostID = Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = 'media'
    MediaID = Column(Integer, primary_key=True)
    MediaType = Column(String(250), nullable=False)
    Media_src = Column(String(500), nullable=False)
    PostID = Column(Integer, primary_key=True)

    

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')