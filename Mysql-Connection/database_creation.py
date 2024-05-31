import mysql.connector as sql_connector


conn=sql_connector.connect(
    user='root',
    password='root',
    port='3306'
)

conn.autocommit=True
cursor=conn.cursor()

query1='DROP DATABASE IF EXISTS mydb'

cursor.execute(query1)

query2='CREATE DATABASE mydb'

cursor.execute(query2)

query3='SHOW DATABASES'

cursor.execute(query3)

print("database", cursor.fetchall())

conn.close()