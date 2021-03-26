#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    _args = sys.argv
    _user = _args[1]
    _passwd = _args[2]
    _db = _args[3]

    data_base = MySQLdb.connect("localhost",
                                _user,
                                _passwd,
                                _db,
                                3306)
    cur = data_base.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON states.id = cities.state_id
    ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
