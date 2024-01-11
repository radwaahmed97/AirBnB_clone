#!/usr/bin/python3
"""BaseModel class"""


import uuid
from datetime import datetime, timedelta
import models

timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializes of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """BaseModel class string representation"""
        print(f"[{str(self.__class__.__name__)}] ({str(self.id)}) {self.__dict__}")

    def save(self):
        """updtates the BaseModel's attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        self.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        return self.__dict__
