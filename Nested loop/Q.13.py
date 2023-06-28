# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     s=i-1
#     while s>0:
#         print(s,end=" ")
#         s=s-1
#     print()
#     i=i+1
n=int(input("Enter a number="))
sum=0
m=1
if n%2==0:
    while n>0:
        sum=sum+n%10
        n=n//10
    print(sum)
else:
    while n>0:
        m=m*(n%10)
        n=n//10
    print(m)
