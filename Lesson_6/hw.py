user=(input("Enter anything but only one symbol or letter or number "))
if len(user) > 1:
    print ("You did not enter one character")
else:
    if ("a" <= user <= "z" ) or ("A" <= user <= "Z" ):
        print ("This is an alphabet")
    else:
        print ("This is not a alphabet")