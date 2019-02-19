#20.Write a function that takes an unsorted integer array as input and
#  returns an array with the duplicates removed.

def Remove(dup): 
    v=[] 
    for i in dup: 
        if i not in v: 
            v.append(i) 
    return v 
      

dup= [2,4,10,20,5,3,2,20,4] 

print(Remove(dup)) 