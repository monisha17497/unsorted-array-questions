#11.Given an unsorted integer array A,find the largest number.

def largest_array(a):
    largest=a[0]
    for i in a:
        if(i>largest):
            largest=i
    return largest
a=[6,7,8,9,4,1]
print(largest_array(a))