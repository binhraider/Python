s = input()
ans = ""
k = 1
for i in range(len(s)) :
  ans = s[-i - 1] + ans
  if k % 3 == 0 : ans = "," + ans
  k += 1
print(ans.strip(','))