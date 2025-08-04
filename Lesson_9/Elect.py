units = float(input("Enter the number of units consumed "))
cost_pu = 0
tax = 0
if units <= 50:
    cost_pu = 2.60
    tax = 25
elif units <= 100:
    cost_pu = 3.25
    tax = 35
elif units <= 200:
    cost_pu = 5.26
    tax = 45
else :
    cost_pu = 8.45
    tax = 75
bil = (units * cost_pu ) +tax
print ("\nElectricity Bill")
print ("--------------------")
print (f"Units comsumed, {units}")
print (f"Cost per units, {cost_pu}")
print (f"Fixed tax, {tax}")
print (f"Total bill, {bil}")
