#!/usr/bin/python3
'''Something usful'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Something more useful'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        exit()

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif not arg == "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] == "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zor = args[0] + "." + args[1]
            if zor not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[zor])

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] == "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zor = args[0] + "." + args[1]
            if zor not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[zor]
                storage.save()
    def do_all(self, arg):
        if arg and not arg == "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            print([str(zor) for zor in storage.all().values()])

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] == "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zorkey = args[0] + "." + args[1]
            if zorkey not in storage.all():
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                elif len(args) < 4:
                    print("** value missing **")
                    return
                else:
                    zorobject = storage.all()[zorkey]
                    try:
                        value = float(args[3])
                        setattr(zorobject, args[2], value)
                    except ValueError:
                        pass
                    try:
                        value = int(args[3])
                        setattr(zorobject, args[2], value)
                    except ValueError:
                        pass
                    setattr(zorobject, args[2], str(value[1:-1]))
                    zorobject.save()

if __name__ == '__main__':
        HBNBCommand().cmdloop()
