from pathlib import Path  # Python 3.6+ only
import os

from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from app import crud, models, schemas
from app.database import SessionLocal, engine

# load_dotenv()
# load_dotenv(verbose=True)
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)


models.Base.metadata.create_all(bind=engine)
origins = ['*']
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/login/", response_model=schemas.User)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):    
    db_user = crud.login(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="invalid username or password")
    return db_user


@app.get('/game/{user_id}/', response_model=schemas.Game)
def get_game(user_id: int, db: Session = Depends(get_db)):
    result = crud.get_game(user_id=user_id, db=db)
    highest_score = crud.get_highest_score(db=db)
    my_best_score = crud.my_best_score(user_id=user_id, db=db)
    return {
        'ran_num': result.ran_num,
        'id': result.id,
        'owner_id': result.owner_id,
        'is_success': result.is_success,
        'move': result.move,
        'highest_score': highest_score,
        'my_best': my_best_score,
    }


@app.post('/game/{user_id}/', response_model=schemas.Game)
def create_game(user_id: int, db: Session = Depends(get_db)):
    return crud.create_game(user_id=user_id, db=db)


@app.patch('/game/{game_id}/', response_model=schemas.Game)
def play_game(game_id: int, input_num: schemas.PlayGame, db: Session = Depends(get_db)):
    result = crud.play_game(db=db, data=input_num, game_id=game_id)
    return result
    