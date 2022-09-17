from importlib.metadata import metadata
from sqlite3 import connect

from sqlalchemy import Table,Column,Integer,String,MetaData

from main import engine
db_response=engine.get_engine.
meta=MetaData(db_response)

create_table=Table(
    'table1',meta,
    Column("N",Integer),
    Column("Ticket count",Integer),
    Column("Movie Name",String),
    Column("Ticket Amount",Integer),
    Column("Net amount(INC GST)",Integer),
)
with db_response.connect() as conn:
    
    create_table.create()
    insert_statement = create_table.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
    conn.execute(insert_statement)

    # Read
    select_statement = create_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = create_table.update().where(create_table.c.year=="2016").values(title = "Some2016Film")
    conn.execute(update_statement)

    # Delete
    delete_statement = create_table.delete().where(create_table.c.year == "2016")
    conn.execute(delete_statement)
# meta.create_all()