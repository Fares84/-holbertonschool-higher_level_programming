#!/usr/bin/python3
""" script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    _args = sys.argv
    _user = _args[1]
    _passwd = _args[2]
    _db = _args[3]
    name = _args[4]

    data_base = MySQLdb.connect("localhost",
                                _user,
                                _passwd,
                                _db,
                                3306)
    cur = data_base.cursor()
    cur.execute("""SELECT * FROM states WHERE name = '{}'
    ORDER BY states.id ASC""".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
