""" Test decorators #1 """

def print_args(function):
    def wrapper(*args, **kwargs):
        print ('Arguments:', args, kwargs)
        return function(*args, **kwargs)
    return wrapper

@print_args
def write(text):
    print (text)

write('foo')

print("-"*80)
# Example 2

def star(fnc):
    def inner(*args,**kwargs):
        print('*'*30)
        fnc(*args,**kwargs)
        print('*'*30)
    return inner

def percent(fnc):
    def inner(*args,**kwargs):
        print('%'*30)
        fnc(*args,**kwargs)
        print('%'*30)
    return inner
# Cascading decorators, a decorator takes a function as arguemnt and must return
# another function as result. Subsitutes the called function with the given function
@star
@percent
def printer(msg):
    print(msg)

printer("asdas")



print(""" Decorator  Example #3""")


# The decorator takes a function as input argument and returns
# a function which calls that function.

def correct_plus5(fnc):
    def wrap(msg):
        return fnc("+{}+".format(msg))
    return wrap

@correct_plus5
def other_print(msg):
    print(msg)

# Call the function
other_print("----")

print("Example #4: a decorator generator")

"""
Passing arguments to decorators
This example demostrates how to pass a parameter to a decorator, to make it
generic
"""

def tags(tag_name):
    def tag_decorator(fnc):
        def fnc_wrapper(string):
            return "<{0}>{1}<{0}>".format(tag_name, fnc(string))
        return fnc_wrapper
    return tag_decorator

@tags("xx")
def catme(text):
    return "test: " + text

print(catme("stuff"))
