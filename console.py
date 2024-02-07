#!/usr/bin/python3
""" Defines class HBNBCommand contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import re
from shlex import split

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Implementation of the command interpreter """

    __classes = {
                "BasaModel",
                "User"
                }
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ exits the program """
        return True

    def do_EOF(self, arg):
        """ Command EOF exits the program """
        return True

    def empty_line(self):
        """ does nothing if empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id
        """
        argt = parse(arg)
        if len(argt) == 0:
            print("** class name missing **")
        elif argt[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argt[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        arg1 = parse(arg)
        objct = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objct:
            print("** no instance found **")
        else:
            print(objct["{}.{}".format(arg1[0], arg[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        arg1 = parse(arg)
        object = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in object:
            print("** no instance found **")
        else:
            del(object["{}.{}".format(arg1[0], arg1[1])])
            storage.save()

    def do_all(self, arg):
        """  Prints all string representation of all instances
            based or not on the class name
        """
        arg1 = parse(arg)
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print("** classes doesn't exist **")
        else:
            object = []
            for objts in storage.all.values():
                if len(arg1) > 0 and arg1 == objts.__class__.__name__:
                    object.append(objts.__str__())
                elif len(arg1) == 0:
                    object.append(objts.__str__())
            print(object)

    def do_update(self, arg):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
        """
        objs = storage.all()
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
            return False
        if arg1[0] not in HBNB.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg1[0], arg1[1]) not in objs:
            print("** no instance found **")
            return False
        if len(arg1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
