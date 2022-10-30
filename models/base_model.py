#!/usr/bin/python3
"""Module's Base Model"""


from uuid import uuid4
from datetime import datetime
import models
from cmd import Cmd

class BaseModel:
    """Base model class"""
    
    def __init__(self, *args, **kwargs):
        """Constructor init"""

        if kwargs is not None and kwargs != {}:
            for k in kwargs.keys():
                self.__dict__[k] = kwargs[k]
                if == 'created_at' or k='updated_at':
                    d_format = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[k] = datetime.strptime(kwargs[k], d_format)
            return

        self.id=str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """Return: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the time now"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary with all key/value pairs of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"]= self.__class__.__name__
        my_dict["created_at"]= my_dict["created_at"].isoformat()
        my_dict["updated_at"]= my_dict["updated_at"].isoformat()
        return my_dict