n = input();
while True:
  x = list(str(n));
  n = 0;
  for i in range(0 , len(x)):
   n += int(x[i])
  if n<10:
   break
print(n)