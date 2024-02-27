#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for k, v in kwargs:
                if k is '__class__':
                    continue
                if '_at' in k:
                    self.__dict__[k] = datetime.fromisoformat(v)
                self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        ndict = self.__dict__.copy()
        ndict['__class__'] = type(self).__name__
        ndict['created_at'] = self.created_at.isoformat()
        ndict['updated_at'] = self.updated_at.isoformat()
        return ndict
