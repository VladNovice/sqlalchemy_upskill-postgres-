# database.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import text, create_engine
from config import settings







sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg, 
    echo=True,
    #pool_size=5,
    #max_overflow=10,
)


# Создаем асинхронный движок
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg, 
    echo=True,
    #pool_size=5,
    #max_overflow=10,
)



session_factory = sessionmaker(sync_engine)

async_session_factory = sessionmaker(async_engine)



class Base(DeclarativeBase):
    pass