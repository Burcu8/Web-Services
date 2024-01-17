from fastapi import FastAPI, APIRouter, HTTPException
from models.models import Content
from database.mongodb import collection
from bson import ObjectId
from routes.route import router


app = FastAPI()

def create_app():
    
    #APIRouter'ı uygulamaya ekle 
    app.include_router(router)
    return app


create_app()