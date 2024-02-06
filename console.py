#!/usr/bin/python3
""" Defines class HBNBCommand contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Implementation of the command interpreter """

    __classes = {"BasaModel"}
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ exits the program """
        return True

    def do_EOF(self, args):
        """ Command EOF exits the program """
        return True

    def empty_line(self):
        """ does nothing if empty line """
        pass

    def do_create(self, args):
        argt = parse(args)
        if len(argt) == 0:
            print("** class name missing **")
        elif argt[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argt[0])().id)
            storage.save()

    def do_show(self, args):
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
            print(object["{}.{}".format(arg1[0], arg[1])])

    def do_destro(self, args):
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

    def do_all(self, args):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
