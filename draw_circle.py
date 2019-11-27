

r = int(input())

def circle_v0(r):
    for y in range(2*r+1):
        oy = y - r
        for x in range(2*r+1):
            ox = x-r
            c = "." if (ox*ox + oy*oy) <= r*r+1 else " "
            print(c, end="")
        print("")


def circle_v1(r):
    #[print("") if ((x-r)**2 + (y-r)**2) < r**2+1 for y in range(2*r+1) for x in range(2*r+1)] 
    circ = lambda  xo, yo : "." if((xo**2 + yo**2) < (r**2+1)) else " "
    [print(circ(x-r,y-r)) for y in range(2*r+1) for x in range(2*r+1)] 

#def int2rom()

def test_test():
    assert True

circle_v1(r)