#6.	Given an unsorted integer array A and an integer value X,
#  return the indices of the locations where X is found in A.

def return_time(a,x):
    count=0
    index=-1
    for i in a:
        if (i==x):
            index=count
            break
        count+=1
    return index
    
a=[2,3,4,5,6,7]
x=int(input("enter the num:"))
print(return_time(a,x))