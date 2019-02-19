#length of the given integer array. Don't use the len() function
def count(array):
    x=0
    for i in array:
        x +=1
    return x
    
array=[1,2,3,4,5]
print (count(array))