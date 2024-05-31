import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    port='3306',
    database='mydb'
)

cursor=conn.cursor()

limit_statement="select * from employee limit 2"

cursor.execute(limit_statement)

print(cursor.fetchall())

offset_statement="select * from employee limit 3 offset 1"

cursor.execute(offset_statement)

print(cursor.fetchall())

conn.close()

