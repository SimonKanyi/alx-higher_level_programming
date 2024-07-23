#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """Represents a City for a MySQL database."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
