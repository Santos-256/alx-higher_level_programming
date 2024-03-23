#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
     # Connect to the MySQL database

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
     # Create a cursor object to execute SQL queries
    cur = db.cursor()
     # Extract the name pattern from the command line argument
    match = sys.argv[4]
     # Execute the SQL query to select states matching the provided name pattern
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
     # Fetch all rows that match the query
    rows = cur.fetchall()
    # print each row
    for row in rows:
        print(row)
         # Close the cursor and database connection
    cur.close()
    db.close()
