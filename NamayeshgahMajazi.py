n = int(input())
counter = 1
for i in range (1,5):
  print("########.......########")
  if n-2>=0:
    print("#ghorfe"+str(counter)+".......ghorfe"+str(counter+1)+"#")
    n-=2
    counter+=2
  elif n==1: 
    print("#ghorfe"+str(counter)+"..............#")
    n-=1
    counter+=1
  else:
    print("#.....................#")
print("#######################")