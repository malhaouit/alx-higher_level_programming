#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa.
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
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
