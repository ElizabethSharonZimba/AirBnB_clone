#!/usr/bin/python3
"""AirBnB Console"""

import cmd
from models import storage
from datetime import datetime
import re


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def precmd(self, line):
        return line.strip()

    def do_EOF(self, line):
        """EOF: End of file. Exits the console."""
        return True

    def do_quit(self, line):
        """quit: Exits the console."""
        return True

    def emptyline(self):
        """If the line is empty, don't do anything."""
        pass

    def do_create(self, line):
        """create: Creates a new instance, saves it, and prints the id."""
        if not line:
            print("** class name missing **")
        else:
            try:
                cls = storage.classes[line]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, line):
        """show: Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """destroy: Deletes an instance based on class name and id."""
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """all: Prints all instances based on class name."""
        if ".all()" in line:
            class_name = line.split(".")[0].strip()
            if class_name in storage.classes:
                print(storage.classes[class_name].all())
            else:
                print("** class doesn't exist **")
        elif not line:
            print([str(v) for v in storage.all().values()])
        elif line not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if line in k])

    def do_update(self, line):
        """update: Updates an instance based on class name and id."""
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                    obj.save()
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """count: Counts the number of instances of a class."""
        if not line:
            print(len([str(v) for v in storage.all().values()]))
        elif line not in storage.classes:
            print("** class doesn't exist **")
        else:
            print(len([str(v) for k, v in storage.all().items()
                       if line in k]))

    def do_show_instance(self, line):
        """show_instance: Retrieves an instance based on its ID."""
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy_instance(self, line):
        """destroy_instance: Destroys an instance based on its ID."""
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_update_attribute(self, line):
        """update_attribute: Updates an instance attribute based on ID."""
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                    obj.save()
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
            else:
                print("** class doesn't exist **")

    def do_update_dictionary(self, line):
        """update_dictionary: Updates an instance based on ID and dictionary."""
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in storage.classes:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            update_dict = eval(line[2])
                        except IndexError:
                            print("** dictionary missing **")
                        else:
                            if not isinstance(update_dict, dict):
                                print("** dictionary missing **")
                            else:
                                for key, value in update_dict.items():
                                    setattr(obj, key, value)
                                obj.save()
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

