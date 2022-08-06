x = []
while True:
  n = int(input())
  x.append(n)
  if n == 0 :
    break
for i in reversed(x):
  if i !=0:
    print(i)