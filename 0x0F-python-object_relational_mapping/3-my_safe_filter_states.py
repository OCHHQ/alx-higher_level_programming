#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database `hbtn_0e_0_usa`.
"""
import sys
import MySQLdb


def main():
    """
    Access the database and retrieve states
    with names starting with 'N'.
    """
    if len(sys.argv) != 4:
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> "
              "<mysql_password> <mysql_database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Use a parameterized query to avoid SQL injection
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE 'N%' "
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
