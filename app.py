from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional

import models
from db import engine, SessionLocal
from exceptions import http_exception

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool


@app.get('/todos')
async def get_all_todos(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get('/todo/{todo_id}')
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()


@app.post('/todo', status_code=201)
async def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return {
        'status': 201,
        'transaction': 'Successful'
    }
