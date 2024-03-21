#!/usr/bin/python3
""" This script lists all states
from the database hbtn_0e_0_usa
"""

import MySQLdb # Importing the MySQLdb module for interacting with MySQL databases
import sys # Importing the sys module for accessing command-line arguments

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor() # Create a cursor object to execute SQL queries
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
