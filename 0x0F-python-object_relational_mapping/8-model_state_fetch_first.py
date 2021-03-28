#!/usr/bin/python3
""" script that prints first State object from the database hbtn_0e_6_usa """
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
                           .format(_user,  _passwd, _db))

    """ the way to issue CREATE is to use create_all() on MetaData object """
    Base.metadata.create_all(engine)

    """  the Session establishes all conversations with the database """
    session = Session(engine)

    """ the entry points to initiate a query against the database """
    # first() returns the first of a potentially larger result set
    # (adding LIMIT 1 to the query), or None if there were no results.
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    print("{}: {}".format(state.id, state.name))
    session.close()
