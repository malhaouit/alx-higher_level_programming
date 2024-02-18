#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class model inherits from Base class (Base = declarative_base()).
    It has two attributes:
        id (int): the unique id for each row.
        name (string): the name of the state in a row.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
