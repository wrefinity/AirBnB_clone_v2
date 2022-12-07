#!/usr/bin/python3
""" defining the base model class for other schemas"""
import uuid
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """ base model for all class schemas"""
    id = Column(String(100), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())

        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
                
            if kwargs.get("updated_at"):
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
                
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)
                    
    def __str__(self):
        """return string representation """
        pass