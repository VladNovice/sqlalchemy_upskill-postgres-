from sqlalchemy import text, insert
from database import sync_engine, async_engine
from models import metadata_obj, worker_table


def get_123_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print(f"{result.first()=}")

async def get_123_async():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT version()"))
        print(f"{result.first()=}")




def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        #stmt = """INSERT INTO workers (username) VALUES
        #    ('AO Bobr'),
        #    ('OOO Volk');"""
        stmt = insert(worker_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volk"},
            ]
        )
        conn.execute(stmt)
        conn.commit()