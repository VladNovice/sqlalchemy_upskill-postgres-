from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

# императивный - легкий стиль
worker_table = Table(
    "workers",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)

