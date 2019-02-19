#prime number
import math
def isprime(N):
    a=True
    for i in range(2,int(math.sqrt(N)+1)):
        if(N%i==0):
         a=False
        break 
    return a
# count the prime num (user input)
def nprime(n):
    count=1
    if(n>=2):
        print 2
    
    i=3
    while(count!=n):
        if(isprime(i)):
            count+=1

        i=i+2
        print(i)

n=int(input("enter the value"))
nprime(n)
