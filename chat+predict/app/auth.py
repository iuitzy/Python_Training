from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import register_user, login_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register")
def show_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def do_register(request: Request, username: str = Form(...), password: str = Form(...)):
    if register_user(username, password):
        return RedirectResponse("/login", status_code=302)
    return templates.TemplateResponse("register.html", {"request": request, "error": "User exists"})

@router.get("/login")
def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def do_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if login_user(username, password):
        response = RedirectResponse("/chat", status_code=302)
        response.set_cookie("user", username)
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
