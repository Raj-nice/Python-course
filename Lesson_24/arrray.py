import array as arr
a = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(a))
print (" Number of occurrences of 3 in the said array: "+ str(a.count(3)))

a.reverse()
print ("Reverse the order of the items:")
print(str(a))
