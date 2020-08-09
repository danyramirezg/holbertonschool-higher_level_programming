#!/usr/bin/python3
""" Cities by states
Take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "INNER JOIN states ON cities.state_id = states.id ORDER BY "
                   "cities.id ASC")
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()
