#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    from MySQLdb import connect
    from sys import argv

    conn = connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    n = cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states ON cities.state_id=states.id\
                    ORDER BY cities.id")
    if (n):
        print(*cur.fetchall(), sep='\n')

    cur.close()
    conn.close()
