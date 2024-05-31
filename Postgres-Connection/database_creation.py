import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cursor=conn.cursor()

query="CREATE database myfirstdb2"

cursor.execute(query)

conn.close()

