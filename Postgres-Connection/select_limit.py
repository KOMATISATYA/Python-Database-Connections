import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    database="mydb"
)

cursor=conn.cursor()

query="select * from employee limit 2 offset 3"

cursor.execute(query)

print(cursor.fetchall())

conn.close()