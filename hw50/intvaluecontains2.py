#2.Given an unsorted integer array A and an integer value X,
#  find if A contains the value X.

def unsorted(A,x):
    
    for i in A:
        if i==x:
            return True
    else:
            return False
A=[2,3,5,7,8,9]
x=int(input("enter the num:"))
print (unsorted(A,x))