n = int(input())
k = n
while True:
  if n%2 == 0:
    n=n/2
    if n%2 != 0:
        break
  else:
    n = (3 * n)+3
if n==1:
  print("Yes")
else:
  print("No")