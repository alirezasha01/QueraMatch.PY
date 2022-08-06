x = int(input())
y = int(input())
def revsNum(number):
 revs_number = 0
 while (number > 0):  
     remainder = number % 10  
     revs_number = (revs_number * 10) + remainder  
     number = number // 10
 return revs_number

if revsNum(x)>revsNum(y):
  print(str(y) + " < " + str(x))
elif revsNum(x)<revsNum(y):
  print(str(x) + " < "+ str(y))
else:
  print(str(x) + " = "+ str(y))