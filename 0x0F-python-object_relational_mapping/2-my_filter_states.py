#!/usr/bin/python3
"""
A script that lists all states in a database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, name, searched = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=name, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id ASC;""",
        (searched,)
    )
    query_rows = cur.fetchall()
    for state in query_rows:
        print(state)
    cur.close()
    conn.close()
