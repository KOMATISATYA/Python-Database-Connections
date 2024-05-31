import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
)

cursor=conn.cursor()

query="select * from employee"

cursor.execute(query)

print(cursor.fetchall())
print(cursor.rowcount)
print(cursor.column_names)

conn.close()