#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id')
    print(*cur.fetchall(), sep='\n')

    cur.close()
    conn.close()
