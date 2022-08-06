x = input()
m = list(x)
g = 0
r = 0
y = 0
for i in range(5):
  if m[i]=="G":
    g+=1
  elif m[i]=="R":
    r+=1
  else:
    y+=1
if (r>=3 or (r>=2 and y>=2) or g==0):
  print("nakhor lite")
else:
  print("rahat baash") 