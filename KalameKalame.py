n = input()
m=list(n)
counter = 0
for i in range (0,len(m)):
  if m[i] == "a" or m[i] == "e" or m[i] == "i" or m[i] == "o" or m[i] == "u" :
    counter+=1
if counter == 0:
  print(1)
else:
  print(pow(2,counter))