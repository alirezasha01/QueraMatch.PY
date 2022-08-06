n = list(input())
for i in range(0,len(n)):
 my_lst_str = ''.join(map(str, n[i:]))
 print(i * str(n[i]) + my_lst_str)