from fastapi import FastAPI, HTTPException
from models.models import Content
from database.mongodb import collection
from bson import ObjectId

app = FastAPI()


#CREATE
@app.post("/content/")
def create_content(content: Content):
    content_id = collection.insert_one(content.model_dump()).inserted_id  #dict() yerine model_dump kullanıldı.
    return {"message": "Content created succesfully", "content_id": str(content_id)}


@app.get("/content/")
def read_contents():
    contents = list(collection.find())
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#READ
@app.get("/content/{content_id}")
def read_contents(content_id: str):
   # return {"content" : []}
    contents = list(collection.find({"_id": ObjectId(content_id)}))
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#UPDATE
@app.put("/content/{content_id}")
def update_content(content_id: int, update_content: Content):
    result = collection.update_one({"_id": content_id}, {"$set": update_content.model_dump()})
    
    if result.modified_count == 1:
        # Get the details of the updated content when the update is successful
        updated_document = collection.find_one({"_id": content_id})
        return {"message": "content updated succesfully", "updated content": updated_document}

    else:
        raise HTTPException(status_code=404, detail = "Content not found")


#DELETE
@app.delete("/content/{content_id}")
def delete_content(content_id: int):
    result = collection.delete_one({"_id": content_id})
    
    if result.deleted_count == 1:
        return {"message": "Content deleted successfully", "deleted_content": result}
    else:
        return HTTPException(status_code=404, detail= "content not found")

