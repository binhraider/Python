import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : 
            return False
    return True

def check(s):
    if nto(len(s)) == False:
        return False
    s1=0
    s2=0
    for c in s:
        if nto(int(c)) == True:
            s1+=1
        else:
            s2+=1
    if s1 > s2:
        return True
    return False




t = int(input())
for i in range(t) :
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    
	
                     