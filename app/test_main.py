import json
from fastapi.testclient import TestClient

from .main import app

TEST = None
client = TestClient(app)
# data = None
# def test_create_user():
#     response = client.post("/users/", json={'username': 'test', 'password': 'test'})    
#     assert response.status_code == 200    
#     user_id = response.json()['id']

def test_get_game():
    # import pdb; pdb.set_trace()
    response = client.get("/game/1/")
    assert response.status_code == 200

def test_play_game():
    response = client.patch("/game/1/", json={'input_num': 3})    
    assert response.status_code == 200

# def test_get_game():    
#     response = client.get("/game/1/")
#     assert response.status_code == 200
#     for i in json.loads(response.json()['ran_num']):
#         if i['id'] == 3:
#             assert i['flip'] == True

def test_play_game():
    response = client.patch("/game/1/", json={'input_num': 4})    
    assert response.status_code == 200


# def test_get_game():    
#     response = client.get("/game/1/")
#     assert response.status_code == 200
#     for i in json.loads(response.json()['ran_num']):
#         if i['id'] == 3 or i['id'] == 4:
#             assert i['flip'] == False
        

# def test_play_game():
#     response = client.patch("/game/1/", json={'input_num': 1})    
#     assert response.status_code == 200

# def test_play_game():
#     response = client.patch("/game/1/", json={'input_num': 7})    
#     assert response.status_code == 200


# def test_get_game():
#     # import pdb; pdb.set_trace()
#     response = client.get("/game/1/")
#     assert response.status_code == 200