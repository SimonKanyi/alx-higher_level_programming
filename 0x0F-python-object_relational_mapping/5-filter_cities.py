#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Create the SQL query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the SQL query, passing the state_name as a parameter to prevent SQL injection
    cur.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # Print each row
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close the cursor and the database connection
    cur.close()
    db.close()
