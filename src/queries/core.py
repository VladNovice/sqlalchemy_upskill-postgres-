from sqlalchemy import text, insert, select
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





class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
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

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(worker_table)
            res = conn.execute(query)
            workers = res.all()
            print(f"{workers=}")

class AsyncCore:
    @staticmethod
    # Асинхронный вариант
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata_obj.drop_all)
            await conn.run_sync(metadata_obj.create_all)



