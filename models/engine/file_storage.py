#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'gaga.json'
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + obj.id] = obj

    def save(self):
        objs = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(objs))

    def reload(self):
        objs = dict()
        try:
            with open(self.__file_path) as f:
                objs = json.load(f)
            self.__objects = {k: BaseModel(**v) for k, v in objs.items()}
        except FileNotFoundError as _:
            pass
