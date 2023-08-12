#!/usr/bin/python3
"""Console for the AirBnB clone project"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
