choice = input("Do you want to shut down your computer? (yes/no): ").strip().lower()
import turtle
if choice == "yes":
    screen = turtle.Screen()
    screen.bgcolor("black")   
    screen.title("Shutting down...")  
    screen.setup(width=1.0, height=1.0)  
    turtle.done()

elif choice == "no":
    print("Sorry! Shutdown canceled ")
else:
    print("Invalid response. Please type 'yes' or 'no'.")