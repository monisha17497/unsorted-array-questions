#15.Write a function that takes two unsorted integer arrays as input
#  and returns True if the two arrays are the same.

n=[]
v=[]
def twoarray(n,v):
    for i in range(0,5):
        a=int(input("enter the value n:"))
        n.append(a)
    for j in range(0,5):
        b=int(input("enter the value v:"))
        v.append(b)
    if (len(n)==len(v)):
            return True
    return False
print(twoarray(n,v))        


