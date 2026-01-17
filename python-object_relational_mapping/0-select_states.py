#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb


if name == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cur:
        print(row)

    cur.close()
    db.close()
