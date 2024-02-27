#!/usr/bin/python3
'''Something usful'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Something more useful'''
    prompt = "(hbnb) "

    def do_quit(self):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self):
        '''EOF command to exit the program'''
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
