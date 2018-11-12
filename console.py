#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
"""entry point for hbnb console"""


class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, clsname=None):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not clsname:
            print('** class name missing **')
        elif not self.clslist.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[clsname]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show instance based on id"""
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid;
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """destroy instance based on id
        """
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid;
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.clslist.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.clslist.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        from datetime import datetime
        from shlex import shlex
        clsname, objid, attrname, attrval = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if len(args) > 2:
            attrname = args[2]
        if len(args) > 3:
            attrval = list(shlex(args[3]))[0].strip('"')
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not attrname:
            print('** attribute name missing **')
        elif not attrval:
            print('** value missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid;
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                obj.__setattr__(attrname,
                                type(obj.__getattribute__(attrname))(attrval))
                obj.updated_at = updatetime
                obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        return True

    def default(self, line):
        """handle class commands"""
        l = line.split('.', 1)
        if len(l) < 2:
            print('*** Unknown syntax:', l[0])
            return False
        clsname, line = l[0], l[1]
        if l[0] not in list(self.clslist.keys()):
            print('*** Unknown syntax: {}.{}'.format(clsname, line))
            return False
        l = line.split('(', 1)
        if len(l) < 2:
            print('*** Unknown syntax: {}.{}'.format(clsname, l[0]))
            return False
        mthname, args = l[0], l[1].rstrip(')')
        if mthname not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(clsname, line))
            return False
        if mthname == 'all':
            self.do_all(clsname)
        elif mthname == 'count':
            print(self.count_class(clsname))
        elif mthname == 'show':
            self.do_show(clsname + " " + args.strip('"'))
        elif mthname == 'destroy':
            self.do_destroy(clsname + " " + args.strip('"'))
        elif mthname == 'update':
            return False
            from shlex import shlex
            l = list(shlex(args, ','))
            print(l)

    def postloop(self):
        """print new line after each loop"""
        print()

    @staticmethod
    def count_class(clsname):
        """count number of objects of type clsname"""
        c = 0
        for k, v in models.storage.all().items():
            if type(v).__name__ == clsname:
                c += 1
        return (c)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
