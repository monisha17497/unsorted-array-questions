#12.Given an unsorted integer array A,
# find the number of times the smallest number is found in the array.

def smallest_array(a):
    small=a[0]
    for i in a:
        if(i<small):
            small=i
        return small

def small(a):
    count=0
    v=smallest_array(a)
    print ("smallest num is",v)
    for i in a:
        if (i==v):
            count+=1
    return count

a=[2,3,4,2,2,2,5,6,]
print("repeated smallest num is:",small(a))

