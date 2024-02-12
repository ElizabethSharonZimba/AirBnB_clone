#!/usr/bin/python3

import cmd
from datetime import datetime
import models
import re


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def precmd(self, line):
        return line.strip()

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[line]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        if not line:
            print([str(v) for v in models.storage.all().values()])
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items() if line in k])

    def do_update(self, line):
        if not line:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr, val = line[2], line[3]
                        except IndexError:
                            print("** attribute name or value missing **")
                        else:
                            try:
                                setattr(obj, attr, val)
                            except AttributeError:
                                print("** cannot set val: {} for attr: ({}) **".format(val, attr))
                            else:
                                obj.save()
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        if not line:
            print(len([str(v) for v in models.storage.all().values()]))
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print(len([str(v) for k, v in models.storage.all().items() if line in k]))

    def do_BaseModel(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'BaseModel', args]))

    def do_User(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'User', args]))

    def do_State(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'State', args]))

    def do_City(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'City', args]))

    def do_Amenity(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Amenity', args]))

    def do_Place(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Place', args]))

    def do_Review(self, line):
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Review', args]))


def parse(line):
    pattern = '\.([^.]+)\(|[\s,()]*([^(),]+)[\s,()]*'
    args = re.findall(pattern, line)
    cmd = args[0][0]
    try:
        args = args[1:]
    except IndexError:
        line = ''
    else:
        line = ' '.join(map(lambda x: x[1].strip('"'), args))
    return cmd, line


if __name__ == '__main__':
    HBNBCommand().cmdloop()

