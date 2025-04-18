import sqlite3
import hashlib

conn = sqlite3.connect('sha1_sql.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Ages;
                  
CREATE TABLE Ages (
    name     VARCHAR(128),
    age   INTEGER
);
''')                  
                  
cur.execute('''INSERT OR IGNORE INTO Ages (name, age)
        VALUES ( ?, ? )''', ('Eduardo', 19 ) )
cur.execute('''INSERT OR IGNORE INTO Ages (name, age)
        VALUES ( ?, ? )''', ('Malachi', 38 ) )
cur.execute('''INSERT OR IGNORE INTO Ages (name, age)
        VALUES ( ?, ? )''', ('Perrie', 23 ) )
cur.execute('''INSERT OR IGNORE INTO Ages (name, age)
        VALUES ( ?, ? )''', ('Rheyden', 36 ) )
cur.execute('''INSERT OR IGNORE INTO Ages (name, age)
        VALUES ( ?, ? )''', ('Maca', 15 ) )
                                   


cur.execute("SELECT name, age FROM Ages")
rows = cur.fetchall()

results_with_hash = []
for name, age in rows:
    # Ensure consistent string representation (especially for age)
    combined_string = f"{name}{age}"
    # Encode to bytes before hashing
    hash_object = hashlib.sha1(combined_string.encode('utf-8'))
    # Get hex representation of the hash
    hex_dig = hash_object.hexdigest()
    results_with_hash.append({'name': name, 'age': age, 'X': hex_dig})

# Now you can sort the results_with_hash list in Python
results_with_hash.sort(key=lambda item: item['X'])

# Print sorted results
for item in results_with_hash:
    print(f"Name: {item['name']}, Age: {item['age']}, SHA1(X): {item['X']}")

conn.close()