

def enhance(func):
    def enh(obj):
        t =  "--->"+ func(obj) + "<---" # remember to call the function
        return t   # ^ is the __repr__ method
    return enh


class base:
    def __init__(self, initial):
        self.name = initial
    @enhance
    def __repr__(self):
        return self.name


if __name__ == "__main__":
    d = base("test")
    print(d)



 # TODO: how to decorate "intercept" a class overloaded attribute
