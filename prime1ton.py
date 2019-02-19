import math
def isprime(n):
    a=True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
            break
        return a

    
def countprimes(n):
    count=0
    if(n>=2):
        print(2)
        count+=1
    for i in range(3,n+1,2):
        if(isprime(i)):
            count+=1
    print(count)

#print("There are {0} prime numbers from 2 to {1}".format(count,n))
n=int(input("enter the number:"))
countprimes(n)




    