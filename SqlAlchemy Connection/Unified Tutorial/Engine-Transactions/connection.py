from sqlalchemy import create_engine,text

engine=create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as con:
    result= con.execute(text("select 'hello world'"))
print(result)