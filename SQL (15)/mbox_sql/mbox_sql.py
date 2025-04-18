import sqlite3

with sqlite3.connect('mboxsql.sqlite') as conn:
    cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Counts;
                  
CREATE TABLE Counts (
    org     TEXT UNIQUE,
    count   INTEGER
);
''')  

handle = open('mbox.txt')

for line in handle:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]
    cur.execute('''INSERT OR IGNORE INTO Counts (org, count)
        VALUES ( ?, 0 )''', ( domain, ) )
    cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                (domain, ))
    # If org entry in db schema is without UNIQUE constraint, the following code should be used to firstly check if the domain already exists
    # and then udpate or insert the count accordingly
    # cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    # row = cur.fetchone()
    # if row is None:
    #     cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    # else:
    #     cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
    
conn.commit()    

cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20')
orgs = cur.fetchall()
d_width = max(len(orgs[0]) for org in orgs) + 5
for org in orgs:
    print(f"{org[0]:<{d_width}} {org[1]}")
