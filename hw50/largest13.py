#13.	Given an unsorted integer array A,
 #find the number of times the largest number is found in the array.

def largestt(a):
    largest=a[0]
    for i in a:
        if(i>largest):
            largest=i
        return largest

def largest(a):
    count=0
    v=largestt(a)
    print ("largest num is",v)
    for i in a:
        if (i==v):
            count+=1
    return count

a=[6,3,4,6,6,6,6,6,]
print("repeated largest num is:",largest(a))