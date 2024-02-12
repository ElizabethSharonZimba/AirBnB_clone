#!/usr/bin/python3
"""
Command interpreter for the AirBnB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance and print its id"""
        args = shlex.split(arg)
        if not args:
            print("Usage: create <class_name>")
        elif args[0] not in storage.classes:
            print("** Class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the details of an instance"""
        args = shlex.split(arg)
        if not args or args[0] not in storage.classes:
            print("Usage: show <class_name> <id>")
        elif len(args) < 2:
            print("** Instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** No instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        args = shlex.split(arg)
        if not args or args[0] not in storage.classes:
            print("Usage: destroy <class_name> <id>")
        elif len(args) < 2:
            print("** Instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** No instance found **")

    def do_all(self, arg):
        """Show all instances or instances of a specific class"""
        args = shlex.split(arg)
        instances = []
        if not args:
            for instance in storage.all().values():
                instances.append(str(instance))
            print(instances)
        elif args[0] not in storage.classes:
            print("** Class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    instances.append(str(value))
            print(instances)

    def do_update(self, arg):
        """Update an instance's attribute"""
        args = shlex.split(arg)
        if not args or args[0] not in storage.classes:
            print("Usage: update <class_name> <id> <attribute_name> <attribute_value>")
        elif len(args) < 3:
            print("** Instance id or attribute name missing **")
        elif len(args) < 4:
            print("** Attribute value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                instance = storage.all()[key]
                attr_name, attr_value = args[2], args[3]
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** No instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

