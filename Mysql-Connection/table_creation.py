import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
    port='3306'
)
conn.autocommit=True

cursor=conn.cursor()

query1='DROP TABLE IF EXISTS EMPLOYEE'

cursor.execute(query1)

create_table = """
                CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
                )
                """
cursor.execute(create_table)

conn.close()