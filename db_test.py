import sqlite3

con = sqlite3.connect('results.db')

cur = con.cursor()

cur.execute('''SELECT * FROM results''')

rows = cur.fetchall()

for row in rows:
    print (row)

con.close()