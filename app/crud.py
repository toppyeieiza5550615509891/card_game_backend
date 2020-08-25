import os
import random
import json

# from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app import models, schemas

RAN_NUM=[
        {'id': 1, 'value': 1, 'flip': False},
        {'id': 2, 'value': 2, 'flip': False},
        {'id': 3, 'value': 3, 'flip': False},
        {'id': 4, 'value': 4, 'flip': False},
        {'id': 5, 'value': 5, 'flip': False},
        {'id': 6, 'value': 6, 'flip': False},
        {'id': 7, 'value': 1, 'flip': False},
        {'id': 8, 'value': 2, 'flip': False},
        {'id': 9, 'value': 3, 'flip': False},
        {'id': 10, 'value': 4, 'flip': False},
        {'id': 11, 'value': 5, 'flip': False},
        {'id': 12, 'value': 6, 'flip': False},
    ]



def random_number():    
    index_ran_num = [*range(0, len(RAN_NUM), 1)]    
    random.shuffle(index_ran_num)    
    return [RAN_NUM[i] for i in index_ran_num]


def get_user_by_email(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login(db: Session, username: str, password: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()    
    if not db_user:
        return False
    if db_user.hashed_password == password + "notreallyhashed":
        return db_user
    else:
        return False


def get_game(user_id: int, db: Session):    
    db_game = db.query(models.Game).filter(models.Game.owner_id == user_id).order_by(-models.Game.id).first()
    if not db_game:
        return create_game(user_id=user_id, db=db)
    new_ran_num = check_flip_card(db_game)
    db_game.ran_num = new_ran_num
    db.commit()
    db.refresh(db_game)
    return db_game

def check_flip_card(db_game):
    ran_num = json.loads(db_game.ran_num)
    temp = []
    dup = []
    diff = set()
    
    for v in ran_num:
        if v['flip'] == True:
            temp.append(v)
    
    if len(temp) % 2 == 0:
        for i in temp:
            if i['value'] not in diff:
                diff.add(i['value'])
            else:
                dup.append(i['value'])
        for i in temp:
            if i['value'] in dup:
                i['flip'] = True
            else:
                i['flip'] = False
        if len(temp) == 12:            
            db_game.is_success = True
        return json.dumps(ran_num)
    else:
        return json.dumps(ran_num)


def play_game(game_id: int, db: Session, data: schemas.PlayGame):    
    input_num = data.input_num
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    my_ran_num = json.loads(db_game.ran_num)
    for k, v in enumerate(my_ran_num):
        if v['id'] == input_num:
            v['flip'] = True
    db_game.ran_num = json.dumps(my_ran_num)
    db_game.move += 1
    db.commit()
    db.refresh(db_game)    
    return db_game


def create_game(user_id: int, db: Session):
    db_game = models.Game(
        ran_num=json.dumps(random_number()),
        owner_id=user_id,        
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
    

def get_highest_score(db: Session):
    db_game = db.query(models.Game).filter(models.Game.is_success == True).order_by(models.Game.move).first()    
    if not db_game:
        return 0
    return db_game.move


def my_best_score(db: Session, user_id: int):
    db_game = db.query(models.Game).filter(models.Game.is_success == True, models.Game.owner_id == user_id).order_by(models.Game.move).first()
    if not db_game:
        return 0
    return db_game.move