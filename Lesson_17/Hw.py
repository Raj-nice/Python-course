
a = input("How much did you pay")
b = input("How much did they ask you for")

def receiving_amount (total_amount, money_needed_to_pay):
    return (total_amount-money_needed_to_pay)

change = receiving_amount(a,b)

print ("Your change is", change)
