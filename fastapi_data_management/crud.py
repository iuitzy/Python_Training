from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user