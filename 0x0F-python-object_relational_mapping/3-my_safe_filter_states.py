#!/usr/bin/python3
""" Take 4 arguments: mysql username, mysql password, database name and state
 name searched (safe from MySQL injection)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %(state)s",
                   {'state': state})
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()
