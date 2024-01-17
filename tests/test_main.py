from fastapi.testclient import TestClient
from pymongo import MongoClient
from main import create_app
from routes.route import router
from models.models import Content
from database.mongodb import collection

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



