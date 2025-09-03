#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa sorted by id."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and print each row
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    conn.close()
