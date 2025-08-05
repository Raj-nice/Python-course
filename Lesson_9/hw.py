user =(input("Do you want to check your age, enter 1 if you want to check your age, and enter 2 if you don't waant to check your age "))
if user == "1":
    print ("\nGreat! now lets check your age.")
    zero_ten = (input("Enter 1 if your age is between 1-10 and enter anything else if it is not your age "))
    if zero_ten== "1":
        print ("Nice, your age is between 1-10")
    else:
        ten_20= (input("Enter 1 if your age is between 10-20 and enter anything else if it is not your age "))
        if ten_20 == "1":
            print ("Nice, your age is between 10-20")
        else:
            t20_30= (input("Enter 1 if your age is between 20-30 and enter anything else if it is not your age "))
            if t20_30 == "1":
                print ("Nice, your age is between 20-30")
            else:
                t30_40 = (input("Enter 1 if your age is between 30-40 and enter anything else if it is not your age "))
                if t30_40 == "1":
                    print ("Nice, your age is between 30-40")
                else:
                    t40_50= (input("Enter 1 if your age is between 40-50 and enter anything else if it is not your age "))
                    if t40_50 == "1":
                        print ("Nice, your age is between 40-50")
                    else:
                        t50_60= (input("Enter 1 if your age is between 50-60 and enter anything else if it is not your age "))
                        if t50_60 == "1":
                            print ("Nice, your age is between 50-60")
                        else:
                            print ("Nice, your age is 60+")
elif user == "2":
    print ("Don't worry, we can find your age another time")
else:
    print ("Invalid Input, try again when you are with your brain.")

