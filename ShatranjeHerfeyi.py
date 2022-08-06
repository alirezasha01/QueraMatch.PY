x = input()
y = x.split(" ")
t = [1 , 1 , 2 , 2 , 2 , 8]
z = ""
for i in range (6):
  k = t[i]-int(y[i])
  z += str(k)+" "
print(z)