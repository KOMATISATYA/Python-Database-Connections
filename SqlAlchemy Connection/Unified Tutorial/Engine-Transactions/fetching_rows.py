from sqlalchemy import create_engine,text

engine=create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as conn:
    conn.execute(text("Create table Sample_table(x int, y int)"))
    conn.execute(text("insert into Sample_table values(:x,:y)"),
                 [{'x':1,"y":2},{'x':3,'y':4}])
    conn.commit()


    result=conn.execute(text("select x,y from Sample_table"))

    # 1.Normal print statement

    for i in result:
        print(f'x={i.x}, y={i.y}')

    # 2.Tuple Assignment

    for x,y in result:
        print("values",x,y)
    
    # 3.Integer index

    for row in result:
        x=row[0]
        y=row[1]
        print(x,y)

    # 4.Attribute Name

    for row in result:
        x=row.x
        y=row.y
        print(x,y)
    
    # 5.Mapping Access

    for dict_row in result.mappings():
        x=dict_row['x']
        y=dict_row['y']
        print(x,y)
