from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, index=True)
    mail = Column(String(255), unique=True, index=True)  # Example length of 255
    password = Column(String(255))  # Example length of 255

    bookmarks = relationship("Bookmark", back_populates="user")

class Bookmark(Base):
    __tablename__ = "Bookmark"
    user_id = Column(Integer, ForeignKey("User.user_id"), primary_key=True, index=True)
    column_id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, unique=True, index=True)
    memo = Column(String(255))  # Example length of 255

    user = relationship("User", back_populates="bookmarks")

class Restaurant(Base):
    __tablename__ = "Restaurant"
    restaurant_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Example length of 255
    longitude = Column(Float)
    latitude = Column(Float)
