print ("Choose your ride")
print ("1. Bike")
print ("2. Car")
ride_type= input("Enter your choice (1 or 2)")
if ride_type == "1":
    print ("\nYou selected: Bike")
    print ("Choose a type of Bike")
    print ("a. Sports Bike")
    print ("b. Electric Bike")
    bike_ty= input("Enter your choice (a or b): ")
    if bike_ty == "a":
        print ("You selected Sports bike")
    elif bike_ty == "b":
        print ("You selected Electric bike")
    else:
        print ("Invalid option")
elif ride_type == "2":
    print ("\nYou selected: Car")
    print ("Choose a type of Car")
    print ("a. Sedan")
    print ("b.SUV")
    car_ty= input("Enter your choice (a or b): ")
    if car_ty == "a":
        print ("You selected Sedan")
    elif car_ty == "b":
        print ("You selected SUV")
    else:
        print ("Invalid option")
else:
    print ("Invalid option")