#!/usr/bin/python3
"""This module lists all states from a MySQL database."""
import sys
import MySQLdb


if __name__ == "__main__":
    conn =MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    
    cursor = conn.cursor()
    cursor.execute(f"USE {sys.argv[4]}")
    cursor.execute("SELECT * FROM  states ORDER BY id ASC")
    rows =cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()






