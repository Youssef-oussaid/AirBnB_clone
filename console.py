#!/usr/bin/python3
"""a console to manipulate the basemodel"""
import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, *args):
        """usage: EOF
            Function: quits the cmdline
        """
        print()
        return True

    def do_quit(self, *args):
        """usage: EOF
            Function: quits the cmdline
        """
        return True

    def do_create(self, line):
        """Usage: create a new instance
            of the class
        """
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_instance = storage.classes()[line]()
                obj_instance.save()
                print(obj_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Shows the instance details of the class
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line_args = line.split(" ")
            if len(line_args) < 2:
                print("** instance id missing **")
            else:
                class_name = line_args[0]
                instance_id = line_args[1]
                if class_name in storage.classes():
                    key = f"{class_name}.{instance.id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance with instance name
            and id and saves to json file
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line_args = line.split(" ")
            if len(line_args) < 2:
                print("** instance id missing **")
            else:
                class_name = line_args[0]
                instance_id = line_args[1]
                if class_name in storage.classes():
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
                        return
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """Usage: it prints the str representation
        of all instances stored.
        """
        instance_obj = storage.all()
        instance_list = []

        if line == "" or line is None:
            for key in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    class_name, instance_id = key.split(".")
                    if line == class_name:
                        instance_list.append(str(value))
                    print(instance_list)

    def do_update(self, line):
        """Usage: it updates the attributes of
        the class
        """
        checks = re.search(r"^(\w+)\s([\S]+?)\s({.+?})$", line)
        if checks:
            class_name = checks.group(1)
            instance_id = checks.group(2)
            update_dict = checks.group(3)

            if class_name is None:
                print("** class name missing **")
            elif instance_id is None:
                print("** instance id missing **")
            elif update_dict is None:
                print("** attribute name missing **")
            else:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all()[key]:
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        update_dict = json.loads(update_dict)

                    attributes = storage.attributes()[class_name]
                    for key, value in update_dict.items():
                        if key in attributes:
                            value = attributes[key](value)
                            setattr(instance_dict, key, value)
                            storage.save
        else:
            checks = re.search(
                r"^(\w+)\s([\S]+?)\s\"(.+?)\"\,\s\"(.+?)\"", line)
            class_name = checks.group(1)
            instance_id = checks.group(2)
            attribute = checks.group(3)
            value = checks.group(4)

            if class_name is None:
                print("** class name missing **")
            elif instance_id is None:
                print("** instance id missing **")
            elif attribute is None:
                print("** attribute name missing **")
            elif value is None:
                print("** value missing **")
            else:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    instance_dict = storage.all()[key]
                    attributes_dict = storage.attributes()[class_name]

                    value = attributes_dict[attribute](
                            value)
                    setattr(instance_dict, attribute, value)
                    storage.save()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
