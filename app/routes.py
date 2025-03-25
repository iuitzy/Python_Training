from fastapi import APIRouter, Depends, HTTPException, Request, Form, Cookie, Response
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.models import User, Transaction
from app.auth import create_jwt_token, verify_jwt_token

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/dashboard")
def dashboard(request: Request, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = access_token.replace("Bearer ", "")
    user_data = verify_jwt_token(token)

    user = db.query(User).filter(User.username == user_data["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token user")

    transactions = db.query(Transaction).filter(Transaction.user_id == user.id).all()

    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user, "transactions": transactions})


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login(
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"sub": user.username})

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)  # ✅ Store JWT in cookie
    return response



@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})



@router.post("/register")
def register(
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=username, password=password, balance=0.0)
    db.add(new_user)
    db.commit()

    return RedirectResponse(url="/login", status_code=303)



@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("access_token")  
    return response



@router.post("/deposit")
def deposit(
    response: Response,
    amount: float = Form(...),
    access_token: str = Cookie(None),
    db: Session = Depends(get_db),
):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = access_token.replace("Bearer ", "")
    user_data = verify_jwt_token(token)

    user = db.query(User).filter(User.username == user_data["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be greater than zero")

   
    user.balance += amount

  
    transaction = Transaction(user_id=user.id, amount=amount, type="deposit")
    db.add(transaction)
    db.commit()

    return RedirectResponse(url="/dashboard", status_code=303)
