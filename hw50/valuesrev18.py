#18.Write a function that takes an unsorted integer array as input and 
# returns an array with the values in reverse order.

v=[]
def copy(v):
    for i in range(0,4):
        a=input("value :")
        v.append(a)
        v.reverse()
    return v
print (copy(v))





