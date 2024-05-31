import psycopg2


conn=psycopg2.connect(
    user='postgres',
    password="Sbksatya@1919",
    database='mydb'
)

cursor=conn.cursor()

query="drop table employee"

cursor.execute(query)

conn.commit()

cursor.execute("select * from employee") #It'll give exception

print(cursor.fetchall())

conn.close()