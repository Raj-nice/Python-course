print ("Mean Value (Average) Calculator ")
count = int(input("How many numbers? "))
total = 0
for i in range(count):
    num = int(input("Enter number "))
    total += num
    

mean = total / count
print("Mean value is" , mean )