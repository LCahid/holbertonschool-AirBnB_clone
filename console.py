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
        elif not arg[0] == "BaseModel":
            print("** class name missing **")
        elif not args[1]:
            print("** instance id missing **")
        elif not args[1] == args[0].id:
            print("** no instance found **")
        else:
            print(storage.all())

if __name__ == '__main__':
        HBNBCommand().cmdloop()
