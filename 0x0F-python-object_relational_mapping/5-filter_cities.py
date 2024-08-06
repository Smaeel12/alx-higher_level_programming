#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()

    state_name = db.string_literal(argv[4]).decode()

    query = f"""SELECT cities.name
                FROM cities
                WHERE cities.state_id = (SELECT id FROM states
                WHERE states.name = {state_name})
                ORDER BY cities.id"""

    cursor.execute(query)
    rows = cursor.fetchall()

    if rows != () and rows is not None:
        for row in rows[:-1]:
            print(row[0], end=', ')
        print(rows[-1][0])
