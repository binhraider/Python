def check(s):
    n=len(s)
    for i in range(1,n):
        if s[i-1]>s[i]:
            return False
    return True

t=int(input())
for i in range(t):
    s=input()
    if check(s) == False:
        print("NO")
    else:
        print("YES")   