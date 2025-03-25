from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/")
def create_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    return crud.create_user(db, schemas.UserCreate(name=name, email=email))