#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
