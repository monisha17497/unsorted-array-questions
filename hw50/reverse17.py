#17.Write a function that takes an unsorted integer array as input and
#  prints the contents of the array in reverse order.

v=[]
y=[]
#count=0
def contents(v):
    for i in range(0,5):
        #count+=1
        #print(count,"value :")
        a=input("value :")
        v.append(a)
    v.reverse()
    return v
y=contents(v)
for i in range (0,len(y)):
     print(y[i])
