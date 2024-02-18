#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument,
and lists all cities of that state.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306)

    cur = db.cursor()
    query = "SELECT cities.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = BINARY %s\
            ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))

    cur.close()
    db.close()
