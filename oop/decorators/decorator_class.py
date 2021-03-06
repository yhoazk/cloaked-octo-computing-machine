def enhance(func):
    def enh(obj):
        t = "--->" + func(obj) + "<---"              # remember to call the function
        return t   # ^ is the __repr__ method
    return enh


class Base:
    def __init__(self, initial):
        self.name = initial

    @enhance
    def __repr__(self):
        return self.name


if __name__ == "__main__":
    d = Base("test")
    print(d)


# TODO: how to decorate "intercept" a class overloaded attribute
'''
The decorator must be callable, which is short means that it must implement the
function __call__ if it's a class.
'''