num = int(input())
counter = 0
keys = []
key = int(input())
keys.append(key)
for i in range (0 , num-1):
	key = int(input())
	keys.append(key)
	if keys[i] != keys[i + 1]:
		   counter += 1
print(counter)