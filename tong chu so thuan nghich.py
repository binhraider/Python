import math

def check(s):
    tong=0
    for c in s:
        tong+=int(c)
    if tong == int(str(tong)[::-1]) and tong > 10:
        return True
    return False

t = int(input())
for i in range(t) :
    s = input()
    if check(s) == True : 
        print("YES")
    else : 
        print("NO")