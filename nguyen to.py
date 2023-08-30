import math

def prime(n):
    if n<2:
        return False
    for i in range (2, math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

t=int(input())
for i in range (t):
    n=int(input())
    s=0
    for i in range (1,n):
        if math.gcd(i,n)==1:
            s+=1
    if prime(s)==True:
        print("YES")
    else:
        print("NO")
