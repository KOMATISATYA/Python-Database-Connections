from sqlalchemy import create_engine,text

engine=create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.begin() as conn:
    conn.execute(text("CREATE TABLE Sample_table(x int,y int)"))
    conn.execute(text("insert into Sample_table(x,y) values(:x,:y)"),
                 [{'x':5,'y':6},{'x':7,'y':8}])