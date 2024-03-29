from fastapi import FastAPI, APIRouter, HTTPException, Path
from models.models import Content
from bson import ObjectId

# APIRouter oluştur
router = APIRouter()

#CREATE
@router.post("/content/")
async def create_content(content: Content):
    from database.mongodb import collection
    #check duplicate content
    existing_content = collection.find_one({"title": content.title})
    if existing_content:
        raise HTTPException(status_code=400, detail="Content with the same title already exists")
    
    content_id = collection.insert_one(dict(content)).inserted_id  
    return {"message": "Content created succesfully", "content_id": str(content_id)}


@router.get("/content/")
async def read_contents():
    from database.mongodb import collection
    contents = list(collection.find())
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#READ DETAIL
@router.get("/content/{content_id}")
async def read_contents(content_id: str):
    from database.mongodb import collection
   # return {"content" : []}
    contents = list(collection.find({"_id": ObjectId(content_id)}))
    for content in contents:
        content["_id"] = str(content["_id"])
    return {"contents": contents}


#UPDATE
@router.put("/content/{content_id}")
async def update_content(content_id: str, update_content: Content):
    from database.mongodb import collection
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
    from database.mongodb import collection
    result = collection.find_one_and_delete({"_id": ObjectId(content_id)})
    result["_id"] = str(result["_id"])

    if result:
        return {"message": "Content deleted successfully", "deleted_content": result}
    else:
        return HTTPException(status_code=404, detail= "content not found")
    