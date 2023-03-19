#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
Or
sudo ./0-select_states.py <..> <..> <..> if
MySQLdb.OperationalError:
(2002, "Can't connect to local MySQL server through socket \
'/var/run/mysqld/mysqld.sock' (13)")
error is encountered on WSL2
"""

import MySQLdb

from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    [print(state) for state in c.fetchall()]

    c.close()
    db.close()
