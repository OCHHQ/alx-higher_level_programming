#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def main():
    """
    Connects to a MySQL database using MySQLdb and lists all states in the 'states' table.
    Arguments:
        sys.argv[1]: MySQL username
        sys.argv[2]: MySQL password
        sys.argv[3]: Database name
    """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def main():
    """
    Connects to a MySQL database using MySQLdb and lists all states in the 'states' table.
    Arguments:
        sys.argv[1]: MySQL username
        sys.argv[2]: MySQL password
        sys.argv[3]: Database name
    """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

