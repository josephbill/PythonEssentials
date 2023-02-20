import sqlite3

# first we create the database
# create a variable to store a reference to the database connection
conn = sqlite3.connect('emobilis.db')
# To create a new table we use the command CREATE TABLE
# when defining table headings include the data type and any other extra info
# to make my table easy for relation models each table will have an id field or an id column which is unique (PRIMARY KEY)
# PRIMARY KEYS : allows access to a specific record
conn.execute('''CREATE TABLE IF NOT EXISTS students(
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL
             );''')


conn.execute('''CREATE TABLE IF NOT EXISTS lectures(
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     staffnumber INTEGER NOT NULL
             );''')


# INSERTING RECORDS TO A TABLE
# when inserting records ensure you use prepared statements
# this will prevent a hacking technique called SQL injection
name = "joseph"
email = "josephbill00@gmail.com"
conn.execute("INSERT INTO students (name,email) VALUES (?,?)", (name, email))
conn.execute("INSERT INTO students (name,email) VALUES (?,?)", ("Mary", "mary@gmail.com"))
# Retrieve the records
# a variable to reference the fetch : so that you can loop the lists data returned sql
cursor = conn.execute("SELECT * FROM students")
print(cursor) #list of data from fetch
# cursor = conn.execute("SELECT id, name, email FROM users")
# printing data from the users table
for row in cursor:
    print("ID : {row[0]}, Name : {row[1]}, Email : {row[2]},")
# Update data in the table
conn.execute("UPDATE students SET name = ? WHERE id = ?", ("New name", 1))
# Delete data from the table
conn.execute("DELETE FROM students WHERE id = ?", (2,))
# commit changes to the db
conn.commit()
# close the connection
conn.close()












