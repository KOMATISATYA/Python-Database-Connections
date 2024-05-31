import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    host="localhost",
    port="5432",
    database="mydb"
)

conn.autocommit=True

cursor=conn.cursor()

drop_table="drop table if exists  employee "

cursor.execute(drop_table)

create_table="""
              create table employee(
              first_name varchar,
              last_name varchar,
              age int,
              gender varchar,
              income float
              )
"""

try:
    # Execute the Query
    cursor.execute(create_table)
    print("Table succssfully created successfully...!")
    
    # Commit the changes to the database.
    conn.commit()

except psycopg2.errors.SyntaxError as e:
    print(f"Syntax Error : {e}")

conn.close()

