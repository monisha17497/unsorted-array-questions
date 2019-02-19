import math
def isprime(n):
    a=True
    i=2
    while (i<n):
        if(n%i==0):
            a=False
            break
    return a
    i+=1

n=input("enter the num:")
isprime(n)

