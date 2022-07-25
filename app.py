from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

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


@app.get('/todos')
async def get_all_todos(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get('/todo/{todo_id}')
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()
