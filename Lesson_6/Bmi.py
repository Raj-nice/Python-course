height = float(input("Enter your height in cm "))
weight = float(input("Enter your weight in kg "))
if height <=20 or weight <=5:
     print ("Stop messing around")
elif weight > height:
     print ("I won't calculate your BMI, because you are severly obese")
elif weight >= 400:
    print ("No need to check, your obese and thats final")
elif height >= 350:
    print ("Do you think you are the tallest man in the world?")
else:
    BMI = weight / (height/100) **2
    if BMI <= 18.5:
        print("You are underweight" ,BMI)
    elif BMI <= 24.9:
        print("You are healthy" ,BMI)
    elif BMI <= 29.9:
        print("You are overweight" ,BMI)
    elif BMI <= 34.9:
        print("You are severely overweight" ,BMI)
    elif BMI <= 39.9:
        print("You are obese" ,BMI)
    else:
        print("You are severely obese" ,BMI)