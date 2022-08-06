n = int(input())
c = True
b = []
for i in range(0,n):
  m = input()
  if m == "CAPS":
    c = not(c)
  elif c == False:
    b.append(m.upper())
  else:
    b.append(m.lower())
print(*b, sep = "")