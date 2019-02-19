#reverse integer
def reverse(n):
    reversenum=0
    while(n>0):
        temp=n%10
        reversenum=reversenum*10+temp
        n=n/10
    print(reversenum)

n=(input("enter the num:"))
reverse(n)
