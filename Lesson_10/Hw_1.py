number = int(input("Enter the number:"))
power = int(input("Enter to the power of:"))

number2 = number
for power in range(1,power):
    number=number2*number 
print(number)
   