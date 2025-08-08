print ("Lets check if the number is a prime number or not ")
prime = int(input("Enter the number to check if it is a prime number or not "))
# total = 2

if prime > 0 and prime <= 2:
    print("This is a prime number")

for total in range (2, prime):


    if prime%total== 0:
        print ("This is not a prime number")
        break
    
    elif total == prime-1:
        print("This is a prime number")
    