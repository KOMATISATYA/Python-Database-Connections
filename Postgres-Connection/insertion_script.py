import psycopg2

conn=psycopg2.connect(
    user="postgres",
    password="Sbksatya@1919",
    port="5432",
    host="localhost",
    database="mydb"
)

cursor=conn.cursor()

insertion_query="""
              insert into employee values('Ramya', 'Rama priya', 27, 'F', 9000),
                ('Vinay', 'Battacharya', 20, 'M', 6000),
                ('Sharukh', 'Sheik', 25, 'M', 8300),
                ('Sarmista', 'Sharma', 26, 'F', 10000),
                ('Tripthi', 'Mishra', 24, 'F', 6000)
"""

cursor.execute(insertion_query)

conn.commit()

cursor.execute("select * from employee")

print(cursor.fetchall())