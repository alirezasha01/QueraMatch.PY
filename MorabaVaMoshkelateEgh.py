import math
m = input().split()
n = int(m[0])
k = int(m[1])
s = input().split()
sum = 0
for i in range (0,len(s)):
  sum+=int(s[i])
r = math.ceil(sum/k)
print(n-r)