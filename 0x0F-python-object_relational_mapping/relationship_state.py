#!/usr/bin/python3
""" python file that contains the class definition of a city
and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State class inherits from Base
    Args:
        Base (object): declarative_base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state")
