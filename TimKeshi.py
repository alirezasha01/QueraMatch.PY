a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
a3=int(input())
b3=int(input())
a=0
b=0
c=0
if a1>=b1:
  a+=b1
else:
  a+=a1
if a2>=b2:
  b+=b2
else:
  b+=a2
if a3>=b3:
  c+=b3
else:
  c+=a3
print(a+b+c)