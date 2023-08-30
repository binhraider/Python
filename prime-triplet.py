import math

p=[True]*(10**6 +1)
def pri():
    p[0]=p[1]=False
    for i in range(2, math.isqrt(10**6 +1)+1):
        if p[i]:
            for j in range (i**2, 10**6 +1,i):
                p[j]=False
    
pri()

for i in range (int(input())):
    n=int(input())
    cnt=0
    for i in range(n-5):
        if (p[i] and p[i+2] and p[i+6] or p[i] and p[i+4] and p[i+6]):
            cnt+=1
    print(cnt)

