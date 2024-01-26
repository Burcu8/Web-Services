from fastapi.testclient import TestClient
from pymongo import MongoClient
from main import create_app
from routes.route import router
from models.models import Content
from database.mongodb import collection
from bson import ObjectId


app = create_app()
client = TestClient(app)

def test_read_contents_success_and_verify_count():

    response = client.get("/content/")
    assert response.status_code == 200

    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db_test"]
    collection = db["films"]
    expected_count = collection.count_documents({})
    assert len(response.json()['films']) == expected_count

def test_create_content_success():
    
    content = {
        "title": "test content5",
        "year": 2021,
        "length": 120,
        "producer": "test producer",
        "description": "test description",
        "genre": "test genre"
    }
    
    response = client.post("/content/", json=content)
    assert response.status_code == 200
    
    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db_test"] 
    collection = db["films"]
    expected_id = collection.find_one(content)["_id"]
    assert response.json()['content_id'] == str(expected_id)

def test_read_details_contents_success_and_verify_count():
    
    response = client.get("/content/656efee0b171fd8c704b2b2c")
    assert response.status_code == 200

    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db_test"]
    collection = db["films"]
    expected_count = collection.count_documents({"_id": ObjectId("656efee0b171fd8c704b2b2c")})
    assert len(response.json()['contents']) == expected_count


def test_update_content_success_and_verify_count():

    content_id = "65a8e1e81f7764917fccdff8"
    content = {
        "title": "test content2",
        "year": 2021,
        "length": 120,
        "producer": "test producer",
        "description": "test description",
        "genre": "test genre"
    }

    response = client.put(f"/content/{content_id}", json=content)
    assert response.status_code == 200
    
    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db_test"]
    collection = db["films"]
    expected_count = collection.count_documents({"_id": ObjectId(content_id)})
    assert expected_count == 1


def test_delete_content_success_and_verify_count():
    
    content_id = "65a8e1e81f7764917fccdff8"
    response = client.delete(f"/content/{content_id}")
    assert response.status_code == 200
        
    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db_test"]
    collection = db["films"]
    expected_count = collection.count_documents({"_id": ObjectId(content_id)})
    assert expected_count == 0