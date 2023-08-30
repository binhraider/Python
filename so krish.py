import math

def gt(n):
    if n==0: 
        return 1
    else:
        return n * gt(n-1)

t=int(input())
for i in range (t):

    n=int(input())
    m=n
    s=0
    while n!=0:
        s+=gt(n%10)
        n=int(n/10)
    if m==s:
        print("Yes")
    else:
        print("No")

