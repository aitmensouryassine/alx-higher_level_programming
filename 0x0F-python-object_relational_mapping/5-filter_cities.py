#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
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
    query = " ".join(["SELECT cities.name FROM cities LEFT JOIN states",
                      "ON cities.state_id = states.id",
                      "WHERE states.name = %(name)s",
                      "ORDER BY cities.id"])

    cur.execute(query, {'name': argv[4]})
    res = cur.fetchall()
    if res:
        for i in range(len(res)):
            if i != len(res) - 1:
                print(res[i][0], end=", ")
        print(res[len(res) - 1][0])
    else:
        print()
    cur.close()
    db.close()
