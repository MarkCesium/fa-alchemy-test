from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from .config import db_url

engine: AsyncEngine = create_async_engine(
    url=db_url,
    echo=True,
)
