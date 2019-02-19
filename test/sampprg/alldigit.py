#all digit of given num N dividies N
def numdivN(n):
    flag=False
    num=n
    while(n>0):
        temp=n%10
        if(num%temp==0):
            flag=True
        else:
            flag=False
        n=n/10
    return flag

n=input("enter the num:")
print(numdivN(n))

#code 2
# def divisibleofallNumbers(N):
#     #sum =0
#     while(N>0):
#         temp = N%10
#         if(N%temp==0):
#             N=N/10
#         else:
#             return "the number can't be divided"
#     return "the Number can be divisible all the integers"