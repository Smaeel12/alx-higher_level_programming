#!/usr/bin/python3

import MySQLdb
from sys import argv

conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id')
print(*cur.fetchall(), sep='\n')

cur.close()
conn.close()
