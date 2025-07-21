height = float(input("Enter your height in cm "))
weight = float(input("Enter your weight in kg "))
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