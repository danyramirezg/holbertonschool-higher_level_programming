#!/usr/bin/python3
""" All cities by state
Take 4 arguments: mysql username, mysql password, database name and state name
(SQL injection free!)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    state_name = (argv[4], )

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON "
                   "cities.state_id = states.id WHERE states.name = %s ORDER"
                   " BY cities.id;", state_name)

    states = []
    for rows in cursor.fetchall():
        states.append(rows[0])
    print(", ".join(states))

    cursor.close()
    db.close()
