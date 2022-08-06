k = int(input())
r = input()
a = [input() for i in range(k)]
b = []
for i in range (k):
  c = a[i].index(r[i])
  if c>=5:
    c = 9-c
  b.append(c)
d=sum(b)
print(d)