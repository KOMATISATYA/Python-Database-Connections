# After installing mysql-connector-python, Import the mysql.connector library.
import mysql.connector 

# Establishing the connection with a database named project (which exists in my database).
conn=mysql.connector.connect(
   user='root',
   password='root',
   database='project',
   host = "127.0.0.1",
   port='3306'
)

# Creating a cursor object using the cursor() method
cursor=conn.cursor()

# Execute a query using the execute() method.
cursor.execute("select version()")

# Fetch a single row
data=cursor.fetchone()

print("connection estabished to : ", data[0]+" MySQL Version")

# Closing the connection
conn.close()