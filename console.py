#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def do_create(self, arg):
        if not arg or arg not in globals():
            print("** class name missing **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args or args[0] not in globals() or len(args) == 1:
            print("** class name missing **" if not args else "** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            print(instances[key] if key in instances else "** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        if not args or args[0] not in globals() or len(args) == 1:
            print("** class name missing **" if not args else "** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        args = arg.split()
        instances = storage.all()
        obj_list = []
        if not arg:
            obj_list = [str(obj) for obj in instances.values()]
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        else:
            obj_list = [str(obj) for key, obj in instances.items() if key.split('.')[0] == args[0]]
        print(obj_list)

    def do_update(self, arg):
        args = arg.split()
        if not args or args[0] not in globals() or len(args) <= 3:
            print("** class name missing **" if not args else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **" if len(args) == 2 else
                  "** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                obj = instances[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

