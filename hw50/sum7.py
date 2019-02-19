#7.	Given an unsorted integer array A,
#  find the sum of all the elements in A.

def sum(a):
    sum=0
    for i in a:
        sum+=i
    return sum
a=[2,3,4,5]
print(sum(a))