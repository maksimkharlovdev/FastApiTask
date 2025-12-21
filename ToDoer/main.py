from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from database import Database

app = FastAPI(title="ToDoer", version="1.0")
db = Database()

@app.get("/")
async def root():
    return {
        "message": "УРААА!",
        "endpoints": {
            "GET /items": "Получить все товары"
        }
    }

@app.get("/tasks")
async def get_all_tasks():
    return db.get()

@app.get("/tasks/{title}")
async def add_task(title):
    return db.get(title)

@app.post("/tasks/{title}")
async def get_items(title):
    return db.add(title)