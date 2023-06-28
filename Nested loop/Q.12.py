j=1
i=1
while i<=4:
    b=1
    while b<=4-i:
        print(" ",end=" ")
        b=b+1
    s=1
    while s<=j:
        print("*",end=" ")
        s=s+1
    print()
    j=j+2
    i=i+1
j=5
i=1
while i<=4:
    b=1
    while b<=i:
        print(" ",end=" ")
        b=b+1
    s=1
    while s<=j:
        print("*",end=" ")
        s=s+1
    print()
    j=j-2
    i=i+1  