from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api.notes.views import router as notes_router
from .core.database import engine
from .core.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        from .core.models.notes import Note

        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    yield


app: FastAPI = FastAPI(
    title="Notes API",
    description="This is a simple test project",
    docs_url="/",
    lifespan=lifespan,
)
app.include_router(notes_router)
