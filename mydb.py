import time
import sqlite3

con = sqlite3.connect('database.db')
sql_update_query = f"""Update accounts set sent = 1 where name = 'sdh0079'"""
curs = con.execute('SELECT * FROM accounts')
curs.execute(sql_update_query)
con.commit()
curs = con.execute('SELECT * FROM accounts')
print("Record Updated successfully ")
rows = curs.fetchall()
curs.close()

for row in rows:
    print(row)
