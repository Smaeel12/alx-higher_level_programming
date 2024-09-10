#!/usr/bin/python3

from MySQLdb import connect
from sys import argv

conn = connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
query = "SELECT * FROM states WHERE name='{}' ORDER BY states.id".format(
    argv[4])
cur.execute(query)
print(*cur.fetchall(), sep='\n')


cur.close()
conn.close()
