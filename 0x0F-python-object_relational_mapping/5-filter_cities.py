#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    from MySQLdb import connect
    from sys import argv

    conn = connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states ON cities.state_id=\
            states.id WHERE states.name=%s ORDER BY cities.id", (argv[4],))

    print(', '.join([r[0] for r in cur.fetchall()]))

    cur.close()
    conn.close()
