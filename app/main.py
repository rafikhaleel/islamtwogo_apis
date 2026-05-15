from fastapi import FastAPI
from app.api.routes.mosque_routes import mosque_router

app = FastAPI(title="IslamTwoGo APIs", version="1.0")

app.include_router(mosque_router)

@app.get("/")
def root():
    return {"message": "Welcome to IslamTwoGo APIs!"}