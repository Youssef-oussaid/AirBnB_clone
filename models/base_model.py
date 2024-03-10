#!/usr/bin/python3
"""The Base Model that has shared attributres"""
import datetime
from models import storage
import uuid


class BaseModel():
    """A class that has shared attributes, all other classes inherit it"""
    def __init__(self, *args, **kwargs):
        """to initialize new instance attributes"""

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                else:
                    if key == "updated_at" or key == "created_at":
                        kwargs[key] = datetime.datetime.strptime(
                                kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """returns the official str representation"""
        return (f"[{self.__class__.__name__}] ({self.id}) \
                {str(self.__dict__)}")

    def save(self):
        """updates the public attribute updated_at"""
        storage.save()
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict with k/v of __dict__"""
        object_dict = {}
        for key in self.__dict__.keys():
            if key not in ("created_at", "updated_at"):
                object_dict[key] = self.__dict__[key]
            else:
                object_dict[key] = datetime.datetime.isoformat(
                        self.__dict__[key])
        object_dict["__class__"] = self.__class__.__name__
        return (object_dict)
