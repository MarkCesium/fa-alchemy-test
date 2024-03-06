from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
    AsyncSession,
)
from asyncio import current_task

from .core.database import engine
from .api.notes import crud


def get_scoped_session():
    return async_scoped_session(
        session_factory=async_sessionmaker(bind=engine, expire_on_commit=False),
        scopefunc=current_task,
    )


async def session_dependency() -> AsyncSession:  # type: ignore
    session = get_scoped_session()
    async with session():
        yield session
        await session.remove()
