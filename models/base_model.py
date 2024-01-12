#!/usr/bin/python3
"""BaseModel class defines common attributes and methods for other classes"""


import uuid
from datetime import datetime
import models

timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initializes of the BaseModel class."""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], timeformat)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], timeformat)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """BaseModel class string representation"""
        return (f"[{str(self.__class__.__name__)}]
                ({str(self.id)}){self.__dict__}")

    def save(self):
        """
        updates the BaseModel's attribute 'updated_at'
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict.keys():
            new_dict["created_at"] = new_dict["created_at"].strftime(timeformat)
        if "updated_at" in new_dict.keys():
            new_dict["updated_at"] = new_dict["updated_at"].strftime(timeformat)

        new_dict["__class__"] = self.__class__.__name__

        return new_dict
