import sqlite3

# Step 1: Connect to SQLite Database
conn = sqlite3.connect('example.db')  # Creates 'example.db' if it doesn't exist
cursor = conn.cursor()

# Step 2: Create a Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE NOT NULL
)
''')

# Step 3: Insert Data
cursor.execute('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', ("Alice", 30, "alice@example.com"))

cursor.execute('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', ("Bob", 25, "bob@example.com"))

# Commit the changes
conn.commit()

# Step 4: Query Data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 5: Close the Connection
conn.close()
