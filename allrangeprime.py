#print m between n prime num

m=input("enter the number m:")
n=input("enter the number n:")
for i in range(m,n+1):
    if i>1:
        for num in range(2,i):
            if(i%num==0):
                break

        else:
            print (i)
    
    #if(m>n):
       # m,n=n,m
#print("prime num between m and n:")