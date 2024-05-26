import mysql.connector

# Establish a connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="restapi"
)

cursor = db.cursor()

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    department VARCHAR(255)
)
"""
cursor.execute(create_table_query)
db.commit()

# Insert data
insert_query = """
INSERT INTO employees (name, age, department)
VALUES (%s, %s, %s)
"""
data = [
    ("John Doe", 30, "HR"),
    ("Jane Smith", 25, "Finance"),
    ("Emily Davis", 35, "IT")
]
cursor.executemany(insert_query, data)
db.commit()
print(f"{cursor.rowcount} records inserted.")

# Read data
select_query = "SELECT * FROM employees"
cursor.execute(select_query)
records = cursor.fetchall()
for record in records:
    print(record)

# Update data
update_query = """
UPDATE employees
SET department = %s
WHERE name = %s
"""
data = ("Marketing", "Jane Smith")
cursor.execute(update_query, data)
db.commit()
print(f"{cursor.rowcount} record(s) updated.")

# Delete data
delete_query = "DELETE FROM employees WHERE name = %s"
data = ("John Doe",)
cursor.execute(delete_query, data)
db.commit()
print(f"{cursor.rowcount} record(s) deleted.")

# Close the connection
cursor.close()
db.close()