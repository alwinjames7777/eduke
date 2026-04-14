import sqlite3
c = sqlite3.connect('db.sqlite3')
res = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print([x[0] for x in res])
