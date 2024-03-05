from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api.notes.views import router as notes_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app: FastAPI = FastAPI(
    title="Notes API",
    description="This is a simple test project",
    docs_url="/",
    lifespan=lifespan,
)
app.include_router(notes_router)
