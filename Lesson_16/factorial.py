def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial.__doc__)
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 3:", factorial(3))
print("The factorial of 4:", factorial(4))
print("The factorial of 5:", factorial(5))
print("The factorial of 6:", factorial(6))
print("The factorial of 7:", factorial(7))
print("The factorial of 8:", factorial(8))
print("The factorial of 9:", factorial(9))