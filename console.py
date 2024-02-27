#!/usr/bin/python3
'''Something usful'''
import cmd


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

if __name__ == '__main__':
        HBNBCommand().cmdloop()
