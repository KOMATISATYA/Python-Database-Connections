import psycopg2

conn=psycopg2.connect(
    user='postgres',
    password='Sbksatya@1919',
    database='mydb'
)

cursor=conn.cursor()

query="select * from employee order by age"

cursor.execute(query)

result=cursor.fetchall()

print(result)

conn.close()