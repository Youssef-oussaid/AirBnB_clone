#!/usr/bin/python3
"""module responsible for storage"""
import datetime
import json
import os


class FileStorage():
    """store and retrieve data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict where all objects are stored"""
        return self.__objects

    def new(self, obj):
        """adds a new object to the dict"""
        objname = obj.__class__.__name__
        objID = obj.id
        key = f"{objname}.{objID}"
        self.__objects[key] = obj

    def save(self):
        """turn the __objects dict to a json file"""
        object_dict = {}
        for key in self.__objects.keys():
            if type(self.__objects[key]) != dict:
                object_dict[key] = self.__objects[key].to_dict()
        file_name = self.__file_path
        with open(file_name, "w", encoding="utf-8") as jsonfile:
            jsonfile.write(json.dumps(object_dict))

    def reload(self):
        """retrieves stored objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") \
                    as my_file:
                object_dict = json.loads(my_file.read())
            final_dict = {}

            for id, dictionary in object_dict.items():
                class_name = dictionary["__class__"]
                final_dict[id] = self.classes()[class_name](**dictionary)
            FileStorage.__objects = final_dict
