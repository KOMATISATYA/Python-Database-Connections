import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    database="mydb"
)

cursor=conn.cursor()

query="delete from employee where last_name='Sheik'"

cursor.execute(query)

conn.commit()

cursor.execute("select * from employee")

print(cursor.fetchall())

conn.close()