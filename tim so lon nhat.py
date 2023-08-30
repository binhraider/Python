import re

t=int(input())
for i in range(t):
    s=input()
    a=re.findall('\d+', s)
    a = [int(i) for i in a]
    print(max(a))
    
