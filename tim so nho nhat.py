import re

t=int(input())
for i in range(t):
    s=input()
    for c in s:
        a=re.findall('\d+', s)
    a = [int(i) for i in a]
    
    print(min(a))
    
