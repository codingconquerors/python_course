To perform basic CRUD (Create, Read, Update, Delete) operations with Python using a MySQL database, you'll need to follow these steps:

1. **Install the MySQL Connector for Python**:
   This library allows Python to interact with MySQL databases.
   ```sh
   pip install mysql-connector-python
   ```

2. **Connect to the MySQL Database**:
   First, establish a connection to your MySQL database.

3. **Create a Table**:
   Define the structure of the table where data will be stored.

4. **Insert Data (Create)**:
   Add new records to the table.

5. **Read Data (Read)**:
   Retrieve and display records from the table.

6. **Update Data (Update)**:
   Modify existing records in the table.

7. **Delete Data (Delete)**:
   Remove records from the table.

### Step-by-Step Example

Here's a complete example demonstrating these CRUD operations.

#### 1. Install MySQL Connector
Make sure you have `mysql-connector-python` installed:
```sh
pip install mysql-connector-python
```

#### 2. Connect to the MySQL Database
```python
import mysql.connector

# Establish a connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = db.cursor()
```

#### 3. Create a Table
```python
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
```

#### 4. Insert Data (Create)
```python
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
```

#### 5. Read Data (Read)
```python
select_query = "SELECT * FROM employees"
cursor.execute(select_query)

# Fetch all records
records = cursor.fetchall()

for record in records:
    print(record)
```

#### 6. Update Data (Update)
```python
update_query = """
UPDATE employees
SET department = %s
WHERE name = %s
"""
data = ("Marketing", "Jane Smith")
cursor.execute(update_query, data)
db.commit()

print(f"{cursor.rowcount} record(s) updated.")
```

#### 7. Delete Data (Delete)
```python
delete_query = "DELETE FROM employees WHERE name = %s"
data = ("John Doe",)
cursor.execute(delete_query, data)
db.commit()

print(f"{cursor.rowcount} record(s) deleted.")
```

### Full Example

Here's the complete example all together:
```python
import mysql.connector

# Establish a connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
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
```

### Summary

This guide shows how to perform basic CRUD operations using Python and MySQL. You learned how to connect to a MySQL database, create a table, and perform insert, read, update, and delete operations. Remember to handle exceptions and close the database connection in a real-world application to ensure proper resource management.