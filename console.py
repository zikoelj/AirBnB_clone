#!/usr/bin/python3
"""
This modual contains the HBNBCommand class that represants the HBNB console
"""
import cmd

from models.base_model import BaseModel
import models
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "
    """ __classes = {
             "BaseModel",
             "User",
             "State",
             "City",
             "Place",
             "Amenity",
             "Review"
             }"""

    def do_quit(self, command):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, command):
        """Exit the program with EOF (Ctrl + D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, command):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        if not command:
            print("** class name missing **")
            return
        try:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, command):
        """Prints the string representation of an instance."""
        args = command.split()
        if not command:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def do_destroy(self, command):
        """Deletes an instance based on the class name and id."""
        args = command.split()
        if not command:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            storage.save()

    def do_update(self, command):
        """Updates an instance based on the class name and id."""
        args = command.split()
        if not command:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        storage.save()

    def do_all(self, command):
        """Prints all string representation of all instances."""
        objs = storage.all()
        if not command:
            print([str(obj) for obj in objs.values()])
        else:
            args = command.split()
        try:
            cls = eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objs.items()
               if key.startswith(args[0])])

    def do_count(self, command):
        """Usage: count <class> or <class>.count().."""
        argl = command.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
