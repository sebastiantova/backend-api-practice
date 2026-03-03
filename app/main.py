from fastapi import FastAPI
from app.models import Task
from app.database import engine, SessionLocal
from app.db_models import Base, TaskDB

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Task API is running (DB enabled)"}

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(TaskDB).all()
        return [{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks]
    finally:
        db.close()

@app.post("/tasks")
def create_task(task: Task):
    db = SessionLocal()
    try:
        new_task = TaskDB(title=task.title, completed=task.completed)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return {"id": new_task.id, "title": new_task.title, "completed": new_task.completed}
    finally:
        db.close()