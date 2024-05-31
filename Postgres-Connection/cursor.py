import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    database="mydb"
)

conn.autocommit = True

# create an object for cursor.
cursor = conn.cursor()

# define the variable with select statement
select_sql = "select * from employee"

# Execute the Query
cursor.execute(select_sql)

# Check the row count
result = cursor.rowcount
print(result)

cursor.execute("INSERT INTO employee VALUES ('Yateesh', 'Chandra', 22, 'M', 19000)")
print(cursor.statusmessage)

# Commit the changes to the database.
conn.commit()