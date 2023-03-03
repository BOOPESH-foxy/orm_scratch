from importlib.metadata import metadata
from sqlite3 import connect
from venv import create
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData
# import main
import docker_connect
engine = create_engine(docker_connect.database_connect)
meta = MetaData()

class table:
    def table_creator_fun():  

        create_table=Table(
            'table1',meta,
            Column("N",Integer),
            Column("Ticket count",Integer),
            Column("Movie Name",String),
            Column("Ticket Amount",Integer),
            Column("Net amount(INC GST)",Integer),
        )
        meta.create_all()
        print(create_table)
        
if __name__ == "__main__":
    # obj_table = table()
    table.table_creator_fun()
