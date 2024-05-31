from sqlalchemy import create_engine,text

engine=create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE Sample_table(x int,y int)"))
    conn.execute(text("Insert into Sample_table(x,y) values(:x, :y)"),
                 [{'x':1,'y':2},{'x':3,'y':4}])
    conn.commit()