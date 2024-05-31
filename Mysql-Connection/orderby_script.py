import mysql.connector

conn= mysql.connector.connect(
    password='root',
    user='root',
    database='mydb',
    port='3306'
)

cursor=conn.cursor()

query="select * from employee order by Age"

cursor.execute(query)

result=cursor.fetchall()

print(result)

cursor.execute("select * from employee order by income")

result2=cursor.fetchall()

print(result2)

conn.close