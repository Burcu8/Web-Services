from fastapi.testclient import TestClient

from routes.route import router
from models.models import Content
from database.mongodb import collection

client = TestClient(router)

def test_read():
    response = client.get("/content/")
    assert response.status_code == 200

    #expected_output = {"contents": []}
    #assert response.json() == expected_output

def test_post():
    response = client.post("/content/")
    assert response.status_code == 200