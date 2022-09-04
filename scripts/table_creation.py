from importlib.metadata import metadata
from sqlite3 import connect

from sqlalchemy import Table,Column,Integer,String,MetaData

from main import engine
engine=engine.ready()

meta=MetaData()
create_table=Table(
    'table1',meta,
    Column("N",Integer),
    Column("Ticket count",Integer),
    Column("Movie Name",String),
    Column("Ticket Amount",Integer),
    Column("Net amount(INC GST)",Integer),
)
meta.create_all(engine)