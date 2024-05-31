from sqlalchemy import create_engine,text

engine=create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as conn:
    conn.execute(text("Create table Sample_table(x int, y int)"))
    conn.execute(text("insert into Sample_table values(:x,:y)"),
                 [{'x':1,"y":2},{'x':3,'y':4}])
    conn.commit()
    
    result = conn.execute(text("SELECT x, y FROM Sample_table WHERE y > :y"), {"y": 2})

    for i in result:
        print(f"x:{i.x},y:{i.y}")