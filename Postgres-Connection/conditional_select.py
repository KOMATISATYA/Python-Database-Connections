import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    port='5432',
    host='localhost',
    database='mydb'
)

cursor=conn.cursor()

conditional_query="select * from employee where age>25"

cursor.execute(conditional_query)

result=cursor.fetchall()
print(result)

conn.close()