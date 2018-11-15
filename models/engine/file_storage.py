#!/usr/bin/python3
"""File Storage Class"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """ FileStorage class to manage instances """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return type(self).__objects

    def new(self, obj):
        """ put object in __objects """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[k] = obj

    def save(self):
        """ save the objects dictionary into file
        make serializable dict objects """
        temp = {}
        for k, v in type(self).__objects.items():
            temp[k] = v.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(temp) + '\n')

    def reload(self):
        """reload objects from file"""

        clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review,
                   'User': User}
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for k, v in temp.items():
                    self.new(clslist[v['__class__']](**v))
        except FileNotFoundError:
            pass
