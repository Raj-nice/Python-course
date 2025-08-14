num = input("Enter a number:")
length = len(num)

if length % 2 !=0:
    middle_digit = int[length // 2]
    print ("The middle digit is:", middle_digit)
    print ("The product is", middle_digit)
else:
    middle1 =int(num[(length // 2)- 1])
    middle2= int(num[(length // 2)])
    print ("The middle digit are:", middle1, "and" , middle2)
    print ("The product is", middle1 * middle2)