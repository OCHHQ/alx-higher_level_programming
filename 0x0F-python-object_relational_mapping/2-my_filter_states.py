#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <mysql_database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query to select states with a name that matches the argument
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()
