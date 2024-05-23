#!/usr/bin/python3
"""
defines State class and an instance Base = declarative_base()
using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    create state class that link to mysql table 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
