#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
