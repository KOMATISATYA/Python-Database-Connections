import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
    port='3306'
)

cursor=conn.cursor()

update_query="update employee set income=income+2000 where first_name='siddu'"

cursor.execute(update_query)

conn.commit()

select_query="select * from employee"

cursor.execute(select_query)

result=cursor.fetchall()

print(result)

conn.close

