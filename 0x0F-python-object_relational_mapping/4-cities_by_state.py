#!/usr/bin/python3

"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import sys
import MySQLdb

def main():
    """
    Connects to the MySQL database and retrieves all cities.
    """
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <mysql_database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the query
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cursor.execute(query)

        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    main()

