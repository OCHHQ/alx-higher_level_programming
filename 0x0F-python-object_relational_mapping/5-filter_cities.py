#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.
"""

import sys
import MySQLdb

def main():
    """
    Accesses the database and gets the cities of a state
    from the database `hbtn_0e_4_usa`.
    """
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <mysql_database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        query = (
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        city_names = [row[0] for row in rows]
        print(", ".join(city_names))

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
