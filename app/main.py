from fastapi import FastAPI
from .routers import notes_router

app: FastAPI = FastAPI()
app.include_router(notes_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
