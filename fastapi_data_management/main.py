from fastapi import FastAPI
from routes import users, dataframe
from database import engine, Base
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(dataframe.router)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html") as f:
        return f.read()