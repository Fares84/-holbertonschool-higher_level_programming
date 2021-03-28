#!/usr/bin/python3
""" script that creates the State California with the City
 San Francisco from the database hbtn_0e_100_usa """
import sys
from sqlalchemy import create_engine
from relationship_state import State, Base
from sqlalchemy.orm import Session
from relationship_city import City

if __name__ == "__main__":
    _args = sys.argv
    _user = _args[1]
    _passwd = _args[2]
    _db = _args[3]
    # exemple: engine = create_engine
    # ("mysql+pymysql://sylvain:passwd@127.0.0.1/
    # db?host=localhost?port=3306")
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(_user, _passwd, _db))

    Base.metadata.create_all(engine)

    session = Session(engine)
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
