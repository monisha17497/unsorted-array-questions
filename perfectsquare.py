import math
def perfectsquare(n):

    x=(math.sqrt(n))
    y=round(x)
    if(x-y==0):
        print("perfect square")
    else:
        print("not perfect square")
        

n=input("enter the number:")
perfectsquare(n)
