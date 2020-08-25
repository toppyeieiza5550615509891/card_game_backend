from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserLogin(UserBase):
    password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    # is_active: bool
    # items: List[Item] = []

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    ran_num: str
    owner_id: int    
    is_success: Optional[bool] = False
    move: int    
    highest_score: Optional[int] = 0
    my_best: Optional[int] = 0


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True


class PlayGame(BaseModel):    
    input_num: int