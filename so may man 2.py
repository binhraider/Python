t=int(input())
for i in range (t):
   a = input()
   s=0
   for i in a :
      if i == '4' or i == '7' : 
         s += 1
   if s == len(a): 
      print("YES")
   else : 
      print("NO")