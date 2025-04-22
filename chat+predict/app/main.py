from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import joblib
from app.chatbot import get_bot_response
from app import auth

app = FastAPI()
app.include_router(auth.router)

templates = Jinja2Templates(directory="templates")
model = joblib.load("models/model.pkl")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return RedirectResponse("/login")

@app.get("/chat", response_class=HTMLResponse)
def chat_page(request: Request):
    user = request.cookies.get("user")
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("chat.html", {"request": request, "user": user})

@app.get("/chat/query")
def chat_response(q: str):
    return {"response": get_bot_response(q)}

scaler = joblib.load("models/scaler.pkl") 

@app.get("/predict", response_class=HTMLResponse)
def predict_page(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})

# @app.post("/predict")
# def predict(age: int = Form(...), salary: float = Form(...), edu: int = Form(...), fscore: float = Form(...)):
#     pred = model.predict([[age, salary, edu, fscore]])[0]
#     return {"LoanApproved": round(pred)}

@app.post("/predict")
def predict(age: int = Form(...), salary: float = Form(...), edu: int = Form(...), fscore: float = Form(...)):
    input_data = [[age, salary, edu, fscore]]
    scaled_input = scaler.transform(input_data)
    pred = model.predict(scaled_input)[0]
    return {"LoanApproved": round(pred)}
