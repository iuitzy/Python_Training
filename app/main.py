from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from app.database import engine, Base 

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static",StaticFiles(directory="app/static"), name="static")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
