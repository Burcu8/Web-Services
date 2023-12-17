from fastapi import FastAPI, APIRouter, HTTPException
from models.models import Content
from database.mongodb import collection
from bson import ObjectId

# APIRouter oluştur
router = APIRouter()

#CREATE
@router.post("/content/")
async def create_content(content: Content):
    content_id = collection.insert_one(dict(content)).inserted_id  
    return {"message": "Content created succesfully", "content_id": str(content_id)}


@router.get("/content/")
async def read_contents():
    contents = list(collection.find())
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#READ DETAIL
@router.get("/content/{content_id}")
async def read_contents(content_id: str):
   # return {"content" : []}
    contents = list(collection.find({"_id": ObjectId(content_id)}))
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#UPDATE
@router.put("/content/{content_id}")
async def update_content(content_id: str, update_content: Content):

    updated_content_dict = update_content.model_dump()
    result = collection.find_one_and_update({"_id": ObjectId(content_id)}, {"$set": updated_content_dict})
    result["_id"] = str(result["_id"])
    
    if result:
        return {"message": "content updated succesfully", "updated content": result}
    else:
        raise HTTPException(status_code=404, detail= "Content not found")

#DELETE
@router.delete("/content/{content_id}")
async def delete_content(content_id: str):
    result = collection.find_one_and_delete({"_id": ObjectId(content_id)})
    result["_id"] = str(result["_id"])

    if result:
        return {"message": "Content deleted successfully", "deleted_content": result}
    else:
        return HTTPException(status_code=404, detail= "content not found")
    