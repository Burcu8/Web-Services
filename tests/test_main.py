from fastapi.testclient import TestClient
from pymongo import MongoClient
from pymongo.collection import Collection
from main import create_app
from routes.route import router
from models.models import Content
from bson import ObjectId
import pytest


app = create_app()
client = TestClient(app)

@pytest.fixture
def mongodb_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["film_db_test"]
    collection = db["films"]
    yield collection
    

def test_read_contents_success_and_verify_count(mongodb_connection: Collection):

    response = client.get("/content/")
    assert response.status_code == 200
    
    expected_count = mongodb_connection.count_documents({})
    assert len(response.json()['contents']) == expected_count

def test_create_content_success(mongodb_connection: Collection):
    
    content = {
        "title": "test content18",
        "year": 2021,
        "length": 120,
        "producer": "test producer",
        "description": "test description",
        "genre": "test genre"
    }
    
    response = client.post("/content/", json=content)
    assert response.status_code == 200
    
    result = mongodb_connection.insert_one(content)
    inserted_id = result.inserted_id
    query_result = mongodb_connection.find_one({"_id": inserted_id})
    assert query_result["title"] == content["title"]

def test_read_details_contents_success_and_verify_count(mongodb_connection: Collection):
    
    response = client.get("/content/65bb7275363f9aca10bb43a1")
    assert response.status_code == 200

    expected_content = mongodb_connection.count_documents({"_id": ObjectId("65bb7275363f9aca10bb43a1")})
    assert len(response.json()['contents']) == expected_content


def test_update_content_success_and_verify_count(mongodb_connection: Collection):

    content_id = "65bb718354db5b5f25b9c375"
    content = {
        "title": "test content3",
        "year": 2021,
        "length": 120,
        "producer": "test producer",
        "description": "test description",
        "genre": "test genre"
    }

    response = client.put(f"/content/{content_id}", json=content)
    assert response.status_code == 200
    
    expected_count = mongodb_connection.count_documents({"_id": ObjectId(content_id)})
    assert expected_count == 1


def test_delete_content_success_and_verify_count(mongodb_connection: Collection):
    
    content_id = "65bb718354db5b5f25b9c375"
    response = client.delete(f"/content/{content_id}")
    assert response.status_code == 200
        
    expected_count = mongodb_connection.count_documents({"_id": ObjectId(content_id)})
    assert expected_count == 0

