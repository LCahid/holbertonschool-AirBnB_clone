#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
