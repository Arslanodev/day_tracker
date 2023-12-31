from typing import List
from datetime import datetime
from pydantic import BaseModel
from uuid import uuid4, UUID


class Task(BaseModel):
    task_id: UUID = uuid4()
    task_name: str
    spent_time: int = 0


class User(BaseModel):
    user_id: UUID
    tasks: List[Task]


class Active_task(BaseModel):
    id: UUID
    created_date: datetime


class Active_tasks(BaseModel):
    active_tasks: List[Active_task]
