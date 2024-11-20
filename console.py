#!usr/bin/python3

import json
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd, Cmd):
    prompt = '(hbnb) '

    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User",
    ]

    def do_create(self, args):


        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_creation = eval(args[0] + 
            models.storage.save()
            print(new_creation.id)

    def do_show(self, args):

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            key = f"{class_name.{instance_id}"

            if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])
                          
