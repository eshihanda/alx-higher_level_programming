#!/usr/bin/python3
"""creates model CIty class"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ create city class that inherits from base """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
