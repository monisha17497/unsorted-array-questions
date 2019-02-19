#prime num
import math
def isprime(N):
    a=True
    for i in range(2,int(math.sqrt(N)+1)):
        if(N%i==0):
         a=False
        break 
    return a
#print all prime num m to n
def PrintPrimesFromMToN(m,n):
    count=0
    if(m==1 or m==2):
        print(2)
        count+=1
        m=3
    if(m%2==0):
        m+=1
    for i in range(m,n+1,2):
        if(Isprime(i)):
            print(i)
            count+=1
        
    if(count==0):
        print("there are no prime num between {0} and {1}".format(m,n))

m=input("enter the num m:")
n=input("enter the num n:")

if(m>n):
    m,n=n,m
print("prime num between m and n:")