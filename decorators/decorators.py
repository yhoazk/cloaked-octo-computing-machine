def print_args(function):
    def wrapper(*args, **kwargs):
        print ('Arguments:', args, kwargs)
        return function(*args, **kwargs)
    return wrapper

@print_args
def write(text):
    print (text)

write('foo')


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

@star
@percent
def printer(msg):
    print(msg)

printer("asdas")


