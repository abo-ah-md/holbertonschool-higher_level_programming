#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted by id.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def main():
    """
    Lists all states from the database hbtn_0e_0_usa sorted by id.
    Usage: ./0-select_states.py <mysql username> <mysql password>
    <database name>
    """
    try:

        if len(sys.argv) != 5:
            print("Usage: ./3-my_safe_filter_states.py <username>\
            <password> <database> <state_name>")
            return
        user1 = sys.argv[1]
        pass1 = sys.argv[2]
        db1 = sys.argv[3]
        match = sys.argv[4]
        database = None
        c = None
        database = MySQLdb.connect(
            port=3306, host="localhost", user=user1, passwd=pass1, db=db1
        )
        c = database.cursor()
        query = "SELECT * FROM states WHERE name  = %s\
                ORDER BY states.id ASC"
        c.execute(query, (match,))
        [print(state) for state in c.fetchall()]
    except MySQLdb.Error as e:
        print(f"Error connecting to databse, {e}")
    finally:
        if len(sys.argv) != 5:
            return
        if c:
            c.close()
        if database:
            database.close()


if __name__ == "__main__":
    main()
