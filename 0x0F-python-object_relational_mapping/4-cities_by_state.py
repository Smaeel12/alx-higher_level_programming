#!/usr/bin/python3
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cursor = conn.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities, states
                   WHERE cities.state_id = states.id
                   ORDER BY cities.id
                   """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
