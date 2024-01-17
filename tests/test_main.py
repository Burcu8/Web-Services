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
    db = dbclient["film_db"]
    collection = db["contents"]
    expected_count = collection.count_documents({})
    assert len(response.json()['contents']) == expected_count



def test_read_details_contents_success_and_verify_count():
    
    response = client.get("/content/656efee0b171fd8c704b2b2c")
    assert response.status_code == 200

    dbclient = MongoClient("mongodb://localhost:27017/")
    db = dbclient["film_db"]
    collection = db["contents"]
    expected_count = collection.count_documents({"_id": ObjectId("656efee0b171fd8c704b2b2c")})
    assert len(response.json()['contents']) == expected_count


def test_update_content_success_and_verify_count():

    content_id = "65a7f1603db16dfbbcdfd0a4"
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
    db = dbclient["film_db"]
    collection = db["contents"]
    expected_count = collection.count_documents({"_id": ObjectId(content_id)})
    assert expected_count == 1
            