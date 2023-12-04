from fastapi import FastAPI, HTTPException
from models.models import Content
from database.mongodb import collection

app = FastAPI()

@app.get("/")

def read_rood():
    return {"message": "Hello, FastAPI!"}


#yeni içerik eklemek içim
@app.post("/content/")
def create_content(content: Content):
    content_id = collection.insert_many(content.model_dump()).inserted_id  #dict() yerine model_dump kullanıldı.
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
    
    if result.modified_count == 1:
        # Get the details of the updated content when the update is successful
        updated_document = collection.find_one({"_id": content_id})
        return {"massage": "content updated succesfully", "updated content": updated_document}

    else:
        raise HTTPException(status_code=404, detail = "Content not found")


#içerik silmek için
@app.delete("/content/{content_id}")
def delete_content(content_id: str):
    result = collection.delete_one({"_id": content_id})
    
    if result.deleted_count == 1:
        return {"message": "Content deleted successfully", "deleted_content": result}
    else:
        return HTTPException(status_code=404, detail= "content not found")

