#10.Given an unsorted integer array A,
#  find the smallest number.

def smallarray(a):
    small=a[0]
    for i in a:
        if (i<small):
            small=i
    return small
   
a=[6,7,8,9,4,1]
print(smallarray(a))

