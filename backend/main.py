from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:password@postgres-service:5432/postgres"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Hello from Backend!"}

@app.post("/items/")
async def create_item(item: Item):
    # For demo, just echo item back, no DB write yet
    return item
