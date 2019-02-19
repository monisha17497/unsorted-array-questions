#14.Given an unsorted integer array A,
#  print the contents of the array in the given format: {arrayindex:value, arrayindex:value}.
#  Note that there is no comma after the last value.

a=[99,88,77,66,55]
for index,value in enumerate(a):
    
    print (index,value)
