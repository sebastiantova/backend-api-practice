from fastapi import FastAPI, HTTPException
from app.models import Task
from app.database import engine, SessionLocal
from app.db_models import Base, TaskDB

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


def task_to_dict(t: TaskDB) -> dict:
    return {"id": t.id, "title": t.title, "completed": t.completed}


@app.get("/")
def read_root():
    return {"message": "Task API is running (DB enabled)"}


@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(TaskDB).all()
        return [task_to_dict(t) for t in tasks]
    finally:
        db.close()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task_to_dict(task)
    finally:
        db.close()


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    db = SessionLocal()
    try:
        new_task = TaskDB(title=task.title, completed=task.completed)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return task_to_dict(new_task)
    finally:
        db.close()


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    db = SessionLocal()
    try:
        existing = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Task not found")

        existing.title = task.title
        existing.completed = task.completed
        db.commit()
        db.refresh(existing)
        return task_to_dict(existing)
    finally:
        db.close()


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    try:
        existing = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Task not found")

        db.delete(existing)
        db.commit()
        return {"message": "Task deleted", "id": task_id}
    finally:
        db.close()