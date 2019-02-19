#3.	Given an unsorted integer array A and an integer value X,
#  return the index at which X is located in A or return -1 if it is not found in A.

def count(a,x):
     index=-1
     count=0
     for i in a:
         if(i==x):
             index=count
             break
         count +=1
     return index

a=[2,4,6,7,8,9]
x=int(input("enter the num:"))
print(count(a,x))