from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from .core.database import engine
from .api.notes import crud


async def session():
    yield async_sessionmaker(bind=engine, expire_on_commit=False)
