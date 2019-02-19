#4.Given an unsorted integer array A and an integer value X, 
# find if X is found more than once in A.

def index(a,x):
    count=0
    for i in a:
        if(i==x):
            count+=1 
            if(count==2):
                return True
    return False

a=[2,3,4,5,2,2]
x=int(input("enter the num:"))
print(index(a,x))
