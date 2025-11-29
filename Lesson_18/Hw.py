try:
    n = int(input("Type your age:"))
    if n%2 == 0:
        print ("Age is even")
    else:
        print("Age is odd")
    
except ValueError:
    print ("Dont put anything except integers")
else:
    print ("Put integers,")
finally:
    print("Now do the right thing")
