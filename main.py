from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

@app.get("/")

def read_rood():
    return {"message": "Hello, FastAPI!"}


# MongoDB bağlantısı
client = MongoClient("mongodb://localhost:27017/")
db = client["film_db"] 
collection = db["contents"]


class Content(BaseModel):
    title: str
    year: int
    length: int
    producer: str
    description: str
    genre: str


#yeni içerik eklemek içim
@app.post("/content/")
def create_content(content: Content):
    content_id = collection.insert_one(content.model_dump()).inserted_id  #dict() yerine model_dump kullanıldı.
    return {"message": "Content created succesfully", "content_id": str(content_id)}


#içerikleri listelemek için
@app.get("/content")
def read_contents():
    contents = list(collection.find())
    return {"contents": contents}


#içerik güncellemek için
@app.put("/content/{content_id}")
def update_content(content_id: str, update_content: Content):
    result = collection.update_one({"_id": content_id}, {"$set": update_content.model_dump()})
    return result

#içerik silmek için
@app.delete("/content/{content_id}")
def delete_content(content_id: str):
    result = collection.delete_one({"_id": content_id})
    return {"message": "Content deleted successfully", "deleted_content": result}
