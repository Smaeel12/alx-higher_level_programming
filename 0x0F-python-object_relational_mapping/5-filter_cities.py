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
    query = "SELECT cities.name FROM cities WHERE cities.state_id LIKE\
            (SELECT states.id FROM states WHERE states.name LIKE %s LIMIT 1)\
            ORDER BY cities.id ASC"
    params = (argv[4],)
    cur.execute(query, params)
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
