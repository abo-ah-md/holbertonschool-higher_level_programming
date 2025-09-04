#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
This version is safe from MySQL injections.
"""
import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and retrieves states
    based on a user-provided name, using a parameterized
    query to prevent SQL injection.
    """
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>\
        <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = None
    cursor = None

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()

        # The key to preventing SQL injection is using parameterized queries.
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and print the results
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}", file=sys.stderr)
        sys.exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
