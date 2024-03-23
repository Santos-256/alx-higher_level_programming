#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
     # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
     # Execute the SQL query to select city names along with their corresponding state names
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
     # Fetch all rows returned by the query
    rows = cur.fetchall()
    # print each row
    for row in rows:
        print(row)
          # Close the cursor and database connection
    cur.close()
    db.close()
