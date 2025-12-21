from fastapi import FastAPI, HTTPException, Body
from database import Database

app = FastAPI(title="ToDoer", version="1.0")
db = Database()

@app.get("/")
async def root():
    return {
        "message": "Welcome!",
        "endpoints": {
            "GET /items": "Get all tasks",
            "GET /items?{...}": "Get task",
            "POST /items": "Add task",
        }
    }

@app.get("/items")
async def get_all_tasks():
    return db.get()

@app.get("/items/{title}")
async def get_task(title):
    try:
        return db.get(title)
    except Exception:
        raise HTTPException(status_code=404, detail="Task not gound")

@app.post("/items")
async def add_task(title:str = Body(...), description:str = Body(...)):
    if description:
        db.add(title, description)
        return {"msg":"Done"}
    else:
        db.add(title)