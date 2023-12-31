from fastapi import FastAPI

from uuid import uuid4, UUID
from day_tracker.models import Task
from datetime import datetime


app = FastAPI()
running_task_database = {}
database = {
    "84fdad0b-2468-472b-be92-4f66bfb0239f": {
        "task_id": "84fdad0b-2468-472b-be92-4f66bfb0239f",
        "task_name": "Learning",
        "spent_time": 0,
    },
    "d0b-2468-472b-be92-4f66bfb0239f": {
        "task_id": "d0b-2468-472b-be92-4f66bfb0239f",
        "task_name": "Reading",
        "spent_time": 0,
    },
}


@app.get("/api/v1/tracker")
def get_task_names():
    global database
    if running_task_database:
        return running_task_database
    else:
        return [value for key, value in database.items()]


@app.get("/api/v1/tracker/{task_id}")
def get_details(task_id):
    return database[task_id]


@app.post("/api/v1/tracker")
def add_new_task(task_data: Task):
    id = uuid4()
    task_data.task_id = id
    database[id] = task_data

    return task_data


@app.delete("/api/v1/tracker/{task_id}")
def delete_task(task_id):
    pass


@app.get("/api/v1/tracker/start/{task_id}")
def start_tracker(task_id):
    global running_task_database
    running_task_database = {"fkey": task_id, "created_date": datetime.now()}

    return running_task_database


@app.get("/api/v1/tracker/stop/")
def stop_tracker():
    global running_task_database
    date = running_task_database["created_date"]
    current = datetime.now()
    running_task_database = {}

    return date - current


@app.get("/api/v1/tracker/{kind}")
def generate_reports(kind):
    pass
