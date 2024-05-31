from sqlalchemy import create_engine,text

pg_engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/mydb", echo=True)

with pg_engine.connect() as conn:
    conn.execute(text("create table Sample(x int, y int)"))
    conn.commit()