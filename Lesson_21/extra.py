number = int(input("How many numbers do you want in the list?: "))
nums = []
total = 0
for i in range (0,number):
    num = int(input("Add a number to your desired list: "))
    nums.append(num)
    total += num
print (nums)

average = total/number

print (round(average, 3))