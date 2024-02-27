#!/usr/bin/python3
import json


class FileStorage:
    __file_path = 'gaga.json'
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + obj.id] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        objs = dict()
        try:
            with open(self.__file_path) as f:
                objs = json.loads(f.read())
        except Exception as _:
            pass
        return objs
