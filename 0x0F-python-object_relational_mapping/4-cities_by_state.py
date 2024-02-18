#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
