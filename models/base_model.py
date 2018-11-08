#!/usr/bin/python3
from models import storage
from uuid import uuid4
from datetime import datetime

"""Base Model Module"""


class BaseModel:
    """Class Base Model"""

    id = str(uuid4())
    datenow = datetime.now()
    created_at = datenow
    updated_at = datenow

    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.id = type(self).id
        self.created_at = type(self).created_at
        self.updated_at = type(self).updated_at
        if kwargs:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at public instance attribute"""
        storage.save()
        updated_at = datetime.now()

    def to_dict(self):
        """Convert object to dictionary representation"""
        dct = self.__dict__
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
