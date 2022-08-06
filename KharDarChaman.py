n = input()
x = n.split(" ")
a = int(x[0])
b = int(x[1])
l = int(x[2])
counter = 0
for i in range (0 , l):
  if i%2 == 0:
    counter+=a
  else:
    counter+=b
print(counter)