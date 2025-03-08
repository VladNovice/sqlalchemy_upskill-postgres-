from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from src.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg, 
    echo=True,  # Консоль будет сыпать все запросы которые делает sql
    pool_size=5,
    max_overflow=10,
)


with engine.begin() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res=}")