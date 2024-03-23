#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

# Check if the script is being run directly
if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

     # Create a cursor object to execute SQL queries
    cur = db.cursor()

     # Execute SQL query to select city names in the specified state
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

     # Fetch all rows returned by the query
    rows = cur.fetchall()

     # Extract city names from the fetched rows and store them in a list
    tmp = list(row[0] for row in rows)

    # Print the city names separated by commas
    print(*tmp, sep=", ")

     # Close the cursor
    cur.close()

     # Close the database connection
    db.close()
