n = int(input())
def calculate_lcm(x, y):
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm
for i in range(1,n):
  if i == 1:
    m = int(input())
  k = int(input())
  m=calculate_lcm(m,k)
print((m+1)%30)