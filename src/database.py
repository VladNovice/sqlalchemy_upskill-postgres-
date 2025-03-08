# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text
from config import settings
import asyncio

# Создаем асинхронный движок
engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg, 
    echo=True,
    pool_size=5,
    max_overflow=10,
)

async def test_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT version()"))
        print("PostgreSQL version:", result.scalar())

if __name__ == "__main__":
    # Запускаем асинхронную функцию через event loop
    asyncio.run(test_connection())