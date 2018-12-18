#!/usr/bin/python -tt

"""
Polimorphism and multiinheritance

En este ejemplo lo que tratamos de ver es que pasa con el
polimorfismo cuando se tiene multiple herencia.

En este caso, parece que toma el metodo de la primera classe
en la lista de herencia
"""

class perro:
    def sound(self):
        print "bark"


class gato:
    def sound (self):
        print "meaow"

class perico:
    def sound(self):
        print "squeech"

class cosa( perico, perro,gato):
    pass

def main():

    X = cosa()
    X.sound()



if __name__ == '__main__':
    main()
