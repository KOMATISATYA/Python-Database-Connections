import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
    port='3306'
)

cursor=conn.cursor()

drop_query="DROP TABLE IF EXISTS EMPLOYEE"

cursor.execute(drop_query)

create_query=""" CREATE TABLE EMPLOYEE(
 FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
)
"""

cursor.execute(create_query)

insert_query = "INSERT INTO EMPLOYEE (first_name, last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s)"
data = [
    ("siddu", "sidda", 21, "M", 20000),
    ("adhi", "komati", 20, "F", 20000),
    ("satya","komati",21,"F",21000)
]
cursor.executemany(insert_query,data)

select_query="SELECT * FROM EMPLOYEE WHERE age>20"

cursor.execute(select_query)

result=cursor.fetchall()

print(result)

conn.close
