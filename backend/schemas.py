from pydantic import BaseModel
from typing import List, Optional

class BookmarkBase(BaseModel):
    user_id: int
    column_id: int
    restaurant_id: int
    memo: Optional[str] = None

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    mail: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    bookmarks: List[Bookmark] = []

    class Config:
        orm_mode = True

class RestaurantBase(BaseModel):
    name: str
    longitude: float
    latitude: float

class RestaurantCreate(RestaurantBase):
    pass

class Restaurant(RestaurantBase):
    restaurant_id: int

    class Config:
        orm_mode = True
