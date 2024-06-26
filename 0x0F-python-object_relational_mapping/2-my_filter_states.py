#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY '{}'\
                 ORDER BY id ASC;".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
