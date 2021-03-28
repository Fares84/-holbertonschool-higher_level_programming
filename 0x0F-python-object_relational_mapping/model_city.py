#!/usr/bin/python3
""" python file that contains the class definition of a city
and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ City class inherits from Base
    Args:
        Base (object): declarative_base
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey("states.id"))
