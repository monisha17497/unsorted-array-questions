# Comment
import math
def isprime(n):
    a=True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
            break
    return a

def firstNprimes(n):
    count=0
    if(n>=2):
        print(2)
        
    i=3
    while(count!=n):
        if(isprime(i)):
            count+=1
        i=i+2
        print(i)   

n=int(input("enter the number:"))
firstNprimes(n)

    