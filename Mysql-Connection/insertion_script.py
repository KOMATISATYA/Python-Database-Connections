import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    database='mydb',
    port='3306'
)
conn.autocommit=True
cursor=conn.cursor()

query1="""INSERT INTO EMPLOYEE 

VALUES("satya","komati",21,"F",20000)

"""

query = "INSERT INTO EMPLOYEE (first_name, last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s)"
data = [
    ("siddu", "sidda", 21, "F", 20000),
    ("adhi", "komati", 20, "F", 20000)
]

try:
  cursor.execute(query1)
  cursor.executemany(query,data)
  conn.commit()
except :
   raise Exception()

 

conn.close()