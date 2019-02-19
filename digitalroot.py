def digitalroot(n):
    root=0

    while(n>0 or root>9):
        if(n==0):
            n=root
            root=0

        root+=n%10
        n=n/10
        
    return root
n=input("enter the number:")
print(digitalroot(n))
