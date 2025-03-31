from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column

from typing import Annotated
import enum
import datetime

from database import Base




intpk = Annotated[int, mapped_column(primary_key=True)]

created_atAn = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))] 
updated_atAn = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow, 
    )]




class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column()

class WorkLoad(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column()
    compensation: Mapped[int | None]
    workload: Mapped[WorkLoad]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete='CASCADE'))
    created_at: Mapped[created_atAn] 
    updated_at: Mapped[updated_atAn] 
    
    

    


















metadata_obj = MetaData()

# императивный - легкий стиль
worker_table = Table(
    "workers",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)


