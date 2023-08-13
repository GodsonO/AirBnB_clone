#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(line):
    curly_braces = re.search(r"\{(.*?)\}", line)
    bracket_match = re.search(r"\[(.*?)\]", line)

    def tokenize_and_append(token, container):
        container.extend([i.strip(",") for i in split(token)])

    result = []

    if curly_braces:
        tokenize_and_append(line[:curly_braces.span()[0]], result)
        result.append(curly_braces.group())

    elif bracket_match:
        tokenize_and_append(line[:bracket_match.span()[0]], result)
        result.append(bracket_match.group())

    else:
        tokenize_and_append(line, result)

    return result


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User, "Amenity": Amenity,
        "Place": Place, "City": City, "Review": Review,
        "State": State
        }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match:
            arg_l = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_l[1])
            if match:
                command = [arg_l[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict:
                    call = "{} {}".format(arg_l[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_l = parse(line)
        if not arg_l:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            print(eval(arg_l[0])().id)
            storage.save()

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_l = parse(line)
        if not arg_l:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(arg_l[0], arg_l[1])])

    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arg_l = parse(line)
        if not arg_l:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(arg_l[0], arg_l[1])]
            storage.save()

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_l = parse(line)
        if arg_l and arg_l[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            obj_l = []
            for obj in (value for value in storage.all().values()):
                if len(arg_l) > 0 and arg_l[0] == obj.__class__.__name__:
                    obj_l.append(obj.__str__())
                elif len(arg_l) == 0:
                    obj_l.append(obj.__str__())
            print(obj_l)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_l = parse(line)
        count = 0
        for obj in (value for value in storage.all().values()):
            if arg_l[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arg_l = parse(line)

        if not arg_l:
            print("** class name missing **")
            return False
        if arg_l[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return False
        if len(arg_l) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_l[0], arg_l[1]) not in storage.all():
            print("** no instance found **")
            return False
        if len(arg_l) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_l) == 4:
            obj = storage.all()["{}.{}".format(arg_l[0], arg_l[1])]
            if arg_l[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_l[2]])
                obj.__dict__[arg_l[2]] = valtype(arg_l[3])
            else:
                obj.__dict__[arg_l[2]] = arg_l[3]
        elif type(eval(arg_l[2])) == dict:
            obj = storage.all()["{}.{}".format(arg_l[0], arg_l[1])]
            for k, v in eval(arg_l[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
