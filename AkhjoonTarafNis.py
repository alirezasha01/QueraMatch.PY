arr = []
for i in range(3):
    a = input()
    b = input()
    c = b.split(" ")
    for j in c:
        arr.append(j)
arr1 = list(set(arr))
print(7-len(arr1))