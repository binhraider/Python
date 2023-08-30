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
    arr=[]
    for i in range(13,n):
        s1 = str(i)
        s2 = ''.join(reversed(s1))
        if s1 !=s2:
            if p[int(s1)] and p[int(s2)]:
                if int(s1) not in arr and int(s2) not in arr and int(s2)<n:
                    arr.append(int(s1))
                    arr.append(int(s2))
    print(*arr)

