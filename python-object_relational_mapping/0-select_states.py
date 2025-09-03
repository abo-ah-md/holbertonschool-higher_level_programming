#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa sorted by id."""

import sys, MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect("localhost", 3306, sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    [print(row) for row in cursor.fetchall()]
    cursor.close(); conn.close()
