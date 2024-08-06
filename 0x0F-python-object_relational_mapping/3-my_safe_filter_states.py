#!/usr/bin/python3
from sys import argv
import MySQLdb
"""
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument and safe from MySQL injections

Here's another implementation using the escape_string method
if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()

    # Properly escape the input
    state_name = conn.escape_string('Arizona').decode()
    query = f"SELECT * FROM states WHERE name = '{state_name}'"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

   cur.close()
    conn.close()
"""
if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()

    # Properly escape the input
    state_name = conn.string_literal('Arizona').decode()
    query = f"""SELECT * FROM states
                WHERE name = {state_name}
                ORDER BY states.id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
