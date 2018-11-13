#!/usr/bin/python3
'''Base Model Module'''

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class Base Model"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        datenow = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datenow
            self.updated_at = datenow
            models.storage.new(self)

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert object to dictionary representation"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
