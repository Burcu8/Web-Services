from fastapi import FastAPI, APIRouter, HTTPException
from models.models import Content
from bson import ObjectId
from pydantic import ConfigDict


from pydantic_settings import BaseSettings, SettingsConfigDict

app = FastAPI()

class Config(BaseSettings):
    app_name: str
    host: str
    port: str
    mongo_client: str
    db_name: str
    collection_name: str
    model_config = SettingsConfigDict(env_file = '.env')

settings = Config()

def print_settings():
    from main import settings
    print(settings.app_name)
    print(settings.host)
    print(settings.port)
    print(settings.mongo_client)
    print(settings.db_name)
    print(settings.collection_name)
print_settings()

def create_app():
    from routes.route import router
    #APIRouter'ı uygulamaya ekle 
    app.include_router(router)
    return app
create_app()