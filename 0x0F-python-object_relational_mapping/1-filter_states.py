#!/usr/bin/python3

"""
This script lists all states with a name starting with 'N' (upper N)
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb


def main():
    """
    Access to the database and get the states
    from the database with names starting with 'N'.
    """

    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> "
              "<mysql_password> <mysql_database>")
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
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
        )
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

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
