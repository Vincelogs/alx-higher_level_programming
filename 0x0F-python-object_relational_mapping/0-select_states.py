#!/usr/bin/python3
# Python scripte to list items from MySQL

import MySQLdb

from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    [print(state) for state in c.fetchall()]

    c.close()
    db.close()
