#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    from MySQLdb import connect
    from sys import argv

    conn = connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}'\
        ORDER BY states.id".format(argv[4])
    n = cur.execute(query)
    if (n):
        print(*cur.fetchall(), sep='\n')

    cur.close()
    conn.close()
