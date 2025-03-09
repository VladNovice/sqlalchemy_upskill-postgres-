from sqlalchemy import text
from database import sync_engine, async_engine
from models import metadata_obj


def get_123_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print(f"{result.first()=}")

async def get_123_async():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT version()"))
        print(f"{result.first()=}")




def create_tables():
    metadata_obj.create_all(sync_engine)