#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel, Base


class User(BaseModel, Base):
    """ a schema for users"""
    __tablename__ = "user"
    email = Column(String(150), nullable=False,)
    password = Column(String(150), nullable=False)
    first_name = Column(String(150))
    last_name = Column(String(150))
