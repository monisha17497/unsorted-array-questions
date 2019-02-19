import math
def isprime(N):
    a=True
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(N)+1)):
        if(N%i==0):
            a=False
            break 
    return a

def kthprime(n):
    count=0
    if(n>=2):
        count+=1
        #print(2)

    i=3
    while(count<n):
        if(isprime(i)):
            count+=1
            if(count==n):
                print(i)
        i=i+1

n=input("enter")
kthprime(n)