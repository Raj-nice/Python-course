# Write a program to find the SI?
print ("Give the values for Simple Interest which you want to find")
Pr= int(input("Enter principal amount (Initial sum of money) "))
Ra= float(input("The rate of interest per year "))
Ti= int(input("The time periods in years "))
Si= (Pr*Ra*Ti)/100
print ("Your simple interest is" , Si)
print( "Your total amout is " , Si + Pr)