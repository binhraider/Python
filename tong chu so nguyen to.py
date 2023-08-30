import math

def nto(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


def check(s):
    tong=0
    for c in s:
        tong+=int(c)
    if nto(tong) == True:
        return True
    return False

t = int(input())
for i in range(t) :
    s = input()
    if check(s) == True : 
        print("YES")
    else : 
        print("NO")