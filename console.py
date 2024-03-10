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

    def EOF(self, *args):
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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()