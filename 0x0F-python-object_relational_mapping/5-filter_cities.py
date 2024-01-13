#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
            )
    cursor = db.cursor()

    # Execute JOIN query to get cities for the specified state
    query = """
    SELECT GROUP_CONCAT(name SEPARATOR ', ')
    FROM cities
    WHERE state_id IN (SELECT id FROM states WHERE name = %s)
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Display results
    if result and result[0]:
        print(result[0])
    else:
        print()

    # Close cursor and database connection
    cursor.close()
    db.close()
