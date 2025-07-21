a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))
if a>b or a<c:
    print("I am using or condition")
elif a<b and a>c:
    print("I am using and condition")
else:
    print("The number is unequal")