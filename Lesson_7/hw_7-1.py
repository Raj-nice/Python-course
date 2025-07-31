user = (input("Enter a letter which you want a ASCII number from "))
if len(user) > 1:
    print ("You did not enter one character")
else:
    print (ord(user))