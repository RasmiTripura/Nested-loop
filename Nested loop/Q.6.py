n=int(input())
j=1
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end=" ")
        b=b+1
    s=1
    while s<=j:
        print("*",end=" ")
        s=s+1
    print()
    j=j+2
    i=i+1