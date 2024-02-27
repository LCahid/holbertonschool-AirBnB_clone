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
        if not args[0]:
            print("** class name missing **")
            return
        elif not args[0] == "BaseModel":
            print("** class name missing **")
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
        if not args[0]:
            print("** class name missing **")
            return
        elif not args[0] == "BaseModel":
            print("** class name missing **")
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

if __name__ == '__main__':
        HBNBCommand().cmdloop()
