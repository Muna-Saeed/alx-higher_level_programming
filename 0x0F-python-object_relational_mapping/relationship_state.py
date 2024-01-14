#!/usr/bin/python3
"""
Module that defines the State class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    State class with attributes id and name, and relationship to City
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
            )
