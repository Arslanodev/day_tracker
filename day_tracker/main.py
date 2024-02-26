from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
import crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


running_tasks = {}


# Dependency2
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Task
@app.post("/users/{user_id}/task/")
def create_task_for_user(
    user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)
):
    return crud.create_user_task(db=db, task=task, user_id=user_id)


@app.get("/users/{user_id}/task/")
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks(db, user_id)


@app.get("/users/{user_id}/task/{task_id}/start/")
def start_tracker(user_id: int, task_id: int):
    pass


@app.get("users/{user_id}/task/stop/")
def stop_tracker(user_id: int):
    pass


@app.get("/api/v1/task/{kind}")
def generate_reports(kind):
    pass
