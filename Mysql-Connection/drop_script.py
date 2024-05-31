import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
    port='3306'
)

cursor=conn.cursor()

drop_query="drop table employee"

cursor.execute(drop_query)

print("deleted...")

cursor.execute("select * from employee") # It will give exception

print(cursor.fetchall())

conn.close()