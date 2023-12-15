from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID
from datetime import datetime


class Task(BaseModel):
    task_id: UUID
    task_name: str
    spent_time: int


class User(BaseModel):
    user_id: UUID
    tasks: List[Task]


class Active_task(BaseModel):
    id: UUID
    created_date: datetime


class Active_tasks(BaseModel):
    active_tasks: List[Active_task]


database = {
    "user_id": uuid4(),
    "tasks": [
        {
            "task_id": uuid4(),
            "task_name": "having a shower",
            "spent_time": 0,
        },
        {
            "task_id": uuid4(),
            "task_name": "having a meal",
            "spent_time": 0,
        },
    ],
}

running_task_database = {
    "fkey": database["tasks"][0]["task_id"],
    "created_date": datetime(2023, 12, 14, 17, 52, 10),
}


app = FastAPI()


@app.get("api/v1/tracker")
def get_task_names():
    pass


@app.post("api/v1/tracker/edit")
def add_new_task():
    pass


@app.get("api/v1/tracker/edit/{task_id}")
def delete_task(task_id):
    pass


@app.get("api/v1/tracker/start/{task_id}")
def start_tracker(task_id):
    pass


@app.get("api/v1/tracker/stop/{task_id}")
def stop_tracker(track_id):
    pass


@app.get("api/v1/tracker/{kind}")
def generate_reports(kind):
    pass
