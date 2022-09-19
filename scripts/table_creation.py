from importlib.metadata import metadata
from sqlite3 import connect

from sqlalchemy import Table,Column,Integer,String,MetaData
# import main
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
