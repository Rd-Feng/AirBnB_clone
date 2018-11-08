#!/usr/bin/python3
import cmd
import models
"""entry point for hbnb console"""


class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
