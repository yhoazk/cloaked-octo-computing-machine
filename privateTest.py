#!/usr/bin/python -tt

class privateTest:
    __cosa = 0 #private attribute
    def __priv(self):
        print "THis will not print unless called form an internal fnc"
        pass
    def notPrivate(self):
        print "private Class"
        pass
    def calling_priv(self):
        self.__priv()
        pass
    
    
    
def main():
    test = privateTest()
    test.notPrivate()
    test.calling_priv()
    print test.__cosa
    ##this will lead to an error
    test.__priv()
    
    
if __name__ == '__main__':
    main()

