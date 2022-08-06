x = input()
a = x.split(" ")
r = int(a[0])
c = int(a[1])
if c>10:
  m = "Left"
  n = 11 - r
  o = 21 - c
else:
  m = "Right"
  n = 11 - r
  o = c
print(m,n,o)