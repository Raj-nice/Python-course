import random

number = random.randint(-100,100)

print ("I will generate a number from 10 to 20, and you have to guess it!")
print("The game ends when you guess correctly \n")

while True:
    guess = input("Give me ur best guess")


    if not guess.isdigit():
        print("Please enter a valid number\n")
        continue 
    else:
        print("Your guess isn't quite right, try again\n")