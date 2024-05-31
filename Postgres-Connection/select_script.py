import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    host="localhost",
    port="5432",
    database="mydb"
)

cursor=conn.cursor()

cursor.execute("select * from employee")

print(cursor.fetchone())
print(cursor.fetchmany(3))
print(cursor.fetchall())

conn.close()