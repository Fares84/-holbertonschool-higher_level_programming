#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa """
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session
from model_city import City

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
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
