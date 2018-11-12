#!/usr/bin/python3
import json
"""File Storage Class"""


class FileStorage:
    """ FileStorage class to manage instances """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return type(self).__objects

    def new(self, obj):
        """ put object in __objects """
        k = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[k] = obj

    def save(self):
        """ save the objects dictionary into file """
        """ make serializable dict objects """
        temp = {}
        for k, v in type(self).__objects.items():
            temp[k] = v.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(temp) + '\n')

    def reload(self):
        from ..base_model import BaseModel
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review
        from ..user import User

        clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review,
                   'User': User}
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                temp = json.loads(f.readline())
                for k, v in temp.items():
                    self.new(clslist[v['__class__']](**v))
        except FileNotFoundError:
            pass
