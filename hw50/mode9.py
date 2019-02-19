#9.	Given an unsorted integer array A,
# find the number that occurs the most or find the mode of the array.

def mode(a):
    count=0
    for i in a:
        count+=1
        if (i<count):
            return i
    return count
    
a=[2,3,4,2,2]
print(mode(a))