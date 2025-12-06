L = [4, 5, 1, 2, 9, 7, 10, 8]
print ("Original List:", L)

count = 0

for i in L:
    count += i

avg = count / len(L)

print("sum = ", count)
print("averge = ", avg)

L.sort()

print("sort:", L)

print("smallest element is:", L[0])

print("largest element is:", L[-1])

