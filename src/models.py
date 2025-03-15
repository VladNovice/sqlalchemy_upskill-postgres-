from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()















































metadata_obj = MetaData()

# императивный - легкий стиль
worker_table = Table(
    "workers",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)


