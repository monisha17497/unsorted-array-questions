#8.	Given an unsorted integer array A, find the mean.
def mean(a):
    sum=0
    count=0
    for i in a:
        sum+=i
        count+=1
    v=sum/count
    return v

a=[2,2,2]
print(mean(a))