import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    database="mydb",
    host="localhost",
    port="5432"
)

conn.autocommit=True
cursor=conn.cursor()

query1="update employee set income=income+2000 where income=6000"

cursor.execute(query1)

conn.commit()

query2="select * from employee"

cursor.execute(query2)

print(cursor.fetchall())

conn.close()