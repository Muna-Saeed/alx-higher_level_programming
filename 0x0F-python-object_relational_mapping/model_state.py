#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv

# Create an instance of the Base class
Base = declarative_base()


class State(Base):
    """Define the State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
