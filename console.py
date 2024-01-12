#!/usr/bin/python3
"""entry point to command line interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter"""

    customprompt = "(hbnb) "
    classes_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self):
        pass

    def do_EOF(self):
        pass

    def do_emptyline(self):
        pass

    def do_nth(self):
        pass

    def help_hbnb(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
