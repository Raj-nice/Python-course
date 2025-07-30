print ("Enter 3 number which you want to know what is the choronlogical order (greatest to least)")
Number1 = int(input("Enter first number "))
Number2 = int(input("Enter second number "))
Number3 = int(input("Enter third number "))
if Number1 >= Number2:
    if Number1 >= Number3:
        if Number2 >= Number3:
            print (f"The chronological order is {Number1}, {Number2},{Number3}")
        else: 
            # Number3 >= Number2
            print (f"The chronological order is  {Number1},{Number3},{Number2}")
    else:
        # Number3>= Number1
        print(f"The chronological order is {Number3},{Number1},{Number2}")
else:
    if Number2 >=Number3:
        if Number1 >= Number3:
            print (f"The chronological order is {Number2},{Number1},{Number3}")
        else:
            print (f"The chronological order is {Number2},{Number3},{Number1}" )
    else:
        print(f"The chronological order is {Number3},{Number2},{Number1}")
    

