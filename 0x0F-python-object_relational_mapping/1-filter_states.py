#!/usr/bin/python3

from MySQLdb import connect
from sys import argv

conn = connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
print(*cur.fetchall(), sep='\n')


cur.close()
conn.close()
