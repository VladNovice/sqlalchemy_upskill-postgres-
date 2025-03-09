# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text, create_engine
from config import settings
import asyncio

# Создаем асинхронный движок
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg, 
    echo=True,
    #pool_size=5,
    #max_overflow=10,
)

sync_engine = create_engine(
    url=settings.DATABASE_URL_asyncpg, 
    echo=False,
    #pool_size=5,
    #max_overflow=10,
)



