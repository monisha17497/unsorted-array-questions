#5.Given an unsorted integer array A and an integer value X,
#  return the number of times X is found in A.

def return_time(a,x):
    count=0
    for i in a:
        if (i==x):
            count+=1
            if(count==a):
                return count
    return count 

a=[2,3,4,5,6,3,3,3,7,8,9,10,3]
x=int(input("enter the num:"))
print(return_time(a,x))