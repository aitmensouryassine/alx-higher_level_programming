#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")

    cur = db.cursor()
    query = " ".join(["SELECT cities.id, cities.name, states.name",
                      "FROM cities INNER JOIN states",
                      "ON cities.state_id = states.id",
                      "ORDER BY cities.id"])

    cur.execute(query)
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
