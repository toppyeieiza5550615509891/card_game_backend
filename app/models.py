from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)    
    
    games = relationship('Game', back_populates='owner')


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    ran_num = Column(String)        
    move = Column(Integer, default=0)
    score = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_success = Column(Boolean, default=False)    

    owner = relationship("User", back_populates="games")