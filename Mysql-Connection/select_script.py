import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='root',
    port='3306',
    database='mydb'
)

cursor = conn.cursor()

query = "SELECT * FROM employee"

try:
    cursor.execute(query)

    # Fetch the first row
    result1 = cursor.fetchone()
    print("fetchone:", result1)

    # Fetch all remaining rows
    result2 = cursor.fetchall()
    print("fetchall:", result2)

    # Move the cursor back to the beginning of the result set
    cursor.execute(query)

    # Fetch the first 3 rows again
    result3 = cursor.fetchmany(3)
    print("fetchmany:", result3)

except Exception as e:
    print("Error:", e)

conn.close()
