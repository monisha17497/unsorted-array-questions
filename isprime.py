#prime number
import math
def isprime(N):
    a=True
    for i in range(2,int(math.sqrt(N)+1)):
        if(N%i==0):
         a=False
        break 
    return a

