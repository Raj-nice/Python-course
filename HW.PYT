user = int(input("Enter a number:"))
add = 0
use = user
if user == 0:
    add = 1
else:
    user = abs(user)
    while user > 0:
        user //= 10
        add += 1

print ("The number of digits in the number", use , " is " , add)