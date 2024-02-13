from fastapi import FastAPI
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

def create_app():
    from routes.route import router
    #APIRouter'ı uygulamaya ekle 
    app.include_router(router)
    return app
create_app()