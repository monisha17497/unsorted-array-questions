def perfectsquaresum(n):
    flag=False
    sum=0
    for i in range(1,n,2):
        sum+=i
        if(sum==n):
            return True
        
    return flag 

n=input("enter the number:")
print(perfectsquaresum(n))
        
