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
    query = "SELECT cities.name FROM cities\
    INNER JOIN states ON states.id=cities.state_id\
    WHERE states.name = %s;"
    cur.execute(query, (searched,))
    query_rows = cur.fetchall()
    tmp = list(row[0] for row in query_rows)
    print(*tmp, sep=", ")
    cur.close()
    conn.close()
