#count
def countdig(n):
    count=0
    while(n>0):
        
        temp=n%10
        if(n%temp==0):
            count+=1
    print("count")

n=(input("enter the num:"))
countdig(n)