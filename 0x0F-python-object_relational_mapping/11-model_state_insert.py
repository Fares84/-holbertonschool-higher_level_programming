#!/usr/bin/python3
""" script that adds State object Louisiana to the database hbtn_0e_6_usa """
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session


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
    _louisiana = State(name="Louisiana")
    session.add(_louisiana)
    session.commit()
    print("{}".format(_louisiana.id))
    session.close()
