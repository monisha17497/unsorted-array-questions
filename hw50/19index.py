#19.	Write a function that takes two unsorted integer arrays as input and
# returns the index upto which they are identical. Return -1 otherwise.
a=[5,6,7,8,9]
x=int(input("enter the num:"))
def indexret(a,x):
    count=0
    index=-1
    for i in a:
        if(i==x):
            index=count
            break
        count+=1
    return index
print("array a :",indexret(a,x))

b=[12,13,14,15,16]
x=int(input("enter the num:"))
def ind(b,x):
    count=0
    index=-1
    for j in b:
        if(j==x):
            index=count
            break
        count+=1
    return index
print("array b:",ind(b,x))
