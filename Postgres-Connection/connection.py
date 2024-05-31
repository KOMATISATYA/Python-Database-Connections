import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    host="localhost",
    port="5432",
    database='mydb'
)

cursor=conn.cursor()

cursor.execute("select version()")

result=cursor.fetchone()

print("connection established \n", result)

conn.close()