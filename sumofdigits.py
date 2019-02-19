def sumofdigits(n):
    sum1=0

    while(n>0):
        dig=n%10
        sum1=sum1+dig
        n=n//10
    return sum1
n=input("enter the number:")
print(sumofdigits(n))
