#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <mysql_database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        print("Connecting to the database...")
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        print("Executing query...")
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()

        print("Fetching results...")
        for row in rows:
            print(row)

        cursor.close()
        db.close()
        print("Connection closed.")

    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()

