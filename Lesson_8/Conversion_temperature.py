user= int(input("Press 1 if you want to convert from farhenheit to celsius and press 2 to  do the opposite "))
if user ==1:
    Fa= int(input("Enter Fahrenheit "))
    Ce = 5*(Fa-32)/9
    print ("The temperature in celsius is" , Ce)
elif user ==2:
    Cel = int(input("Enter Celsius "))
    Far =  (Cel*9/5) + 32 
    print ("The temperature in Fahrenheit is" , Far)

else:
    print ("Put either one or two")