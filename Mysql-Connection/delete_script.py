import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    port='3306',
    database='mydb'
)

cursor=conn.cursor()
try:

   delete_query="delete from employee where first_name='siddu'"

   cursor.execute(delete_query)
except:
   conn.rollback()

cursor.execute("select * from employee")

print(cursor.fetchall())

conn.close()