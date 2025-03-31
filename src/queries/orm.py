from sqlalchemy import text, insert
from database import sync_engine, async_engine, session_factory, async_session_factory
from models import metadata_obj, WorkersOrm





def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

def insert_workers():
    with session_factory() as session: 
        worker_arthur = WorkersOrm(username="Arthur")
        worker_vlad = WorkersOrm(username="Vlad")
        session.add_all([worker_vlad, worker_arthur])
        session.commit()

async def insert_data():
    async with session_factory() as session: 
        worker_arthur = WorkersOrm(username="Arthur")
        worker_vlad = WorkersOrm(username="Vlad")
        session.add_all([worker_vlad, worker_arthur])
        await session.commit()