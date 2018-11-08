#!/usr/bin/python3
import json
"""File Storage Class"""


class FileStorage:
    """ FileStorage class to manage instances """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return self.__objects

    def new(self, obj):
        """ put object in __objects """
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """ save the objects dictionary into file """
        """ make serializable dict objects """
        temp = {}
        for k, v in self.__objects.items():
            temp[k] = str(v)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(temp))

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.loads(f.readline())
        except FileNotFoundError:
            pass
