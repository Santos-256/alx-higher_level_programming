#!/usr/bin/python3
"""
Contains the class definition of a City
"""
# Importing required modules from SQLAlchemy
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Defining the City class representing cities in the database
class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    # Foreign key column referencing the id column of the states table
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
