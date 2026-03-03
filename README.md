Task Management API (FastAPI + SQLite)

Backend REST API for managing tasks. Built with FastAPI, Pydantic validation, and SQLite persistence using SQLAlchemy ORM.

Tech Stack

Python

FastAPI

Pydantic

SQLAlchemy

SQLite

Uvicorn

Features

CRUD operations for tasks

Data validation with Pydantic

Persistent storage with SQLite

Auto-generated API docs with Swagger (OpenAPI)

Project Structure

backend-api-practice/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── db_models.py
├── requirements.txt
├── .gitignore

Run Locally
1) Create and activate virtual environment
py -m venv venv
venv\Scripts\activate

2) Install dependencies
pip install -r requirements.txt

3) Run the API server
uvicorn app.main:app --reload

The server will start at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

http://127.0.0.1:8000/docs

Alternative ReDoc documentation:

http://127.0.0.1:8000/redoc
API Endpoints
Get all tasks
GET /tasks

Returns a list of all tasks.

Example response:

[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  }
]

Get a task by ID
GET /tasks/{task_id}

Example:

GET /tasks/1

Create a task
POST /tasks

Example request body:

{
  "title": "Build FastAPI project",
  "completed": false
}

Update a task
PUT /tasks/{task_id}

Example request:

{
  "title": "Build FastAPI project",
  "completed": true
}

Delete a task
DELETE /tasks/{task_id}

Example:

DELETE /tasks/1

Response:

{
  "message": "Task deleted",
  "id": 1
}

Author

Sebastian Valverde Torres
Computer Engineering Student
GitHub: https://github.com/sebastiantova