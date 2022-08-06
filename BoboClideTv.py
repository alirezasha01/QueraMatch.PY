a = input()
x = a.split()
a = int(x[0])
b = int(x[1])
c=int(x[2])
y=[]
counter = 0
for i in range (0,a):
  d = input()
  y.append(d)

for i in range (b , c+b):
   if i%a == 0:
       counter+=1
print(y[i-(counter*a)])
