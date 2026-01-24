numbers1 = [1,2,3]
number2 = [4,5,6]
result = map(lambda x, y: x + y, numbers1, number2)
print (" Addition of two lists")
print (list(result))

nums = [1,2,3,4,5]
def square(x):
    return x*x
square = list(map(square, nums))
print("Square of numbers in list")
print(square)