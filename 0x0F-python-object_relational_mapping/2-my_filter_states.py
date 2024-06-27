#!/usr/bin/python3


"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""


import sys
import MySQLdb


def main():
    """
    Connects to the MySQL database and retrieves states
    based on user input for state name.
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> "
              "<mysql_password> <mysql_database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Construct the SQL query with user input
        query = (
            "SELECT * FROM states "
            "WHERE name = %s "
            "ORDER BY id ASC"
        )
        cursor.execute(query, (state_name,))

        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error {}: {}".format(
            e.args[0],
            e.args[1]
        ))
        sys.exit(1)


if __name__ == "__main__":
    main()


# Add a blank line here to fix the W391 warning
