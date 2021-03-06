#!/usr/bin/python3
"""Take 4 arguments: mysql username, mysql password, database name and state
 name searched (no argument validation needed"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}'"
                   "ORDER BY states.id ASC".format(state))
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()
