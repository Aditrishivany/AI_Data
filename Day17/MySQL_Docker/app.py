import mysql.connector
import os
import time

# Wait for MySQL container to be ready
time.sleep(15)

connection = mysql.connector.connect(
    host="mysql",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print("Company Employees:")
for row in rows:
    print(row)

connection.close()
