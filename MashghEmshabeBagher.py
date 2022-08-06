a= input()
x=a.split(" ")
if int(x[0]) !=0 and  int(x[1]) !=0 and int(x[2]) != 0 and int(x[0])+int(x[1])+int(x[2])==180:
  print("Yes")
else:
  print("No")