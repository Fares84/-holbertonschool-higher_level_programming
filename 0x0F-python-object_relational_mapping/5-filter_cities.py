#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_us
"""
import MySQLdb
import sys

if __name__ == "__main__":
    _args = sys.argv
    _user = _args[1]
    _passwd = _args[2]
    _db = _args[3]
    _statename = _args[4]

    data_base = MySQLdb.connect("localhost",
                                _user,
                                _passwd,
                                _db,
                                3306)
    cur = data_base.cursor()
    cmd = ("""SELECT cities.name FROM cities INNER JOIN states ON
    states.id = cities.state_id WHERE states.name=%s ORDER BY cities.id ASC""")
    cur.execute(cmd, (_statename,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    data_base.close()
