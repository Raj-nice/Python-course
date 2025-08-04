med = input("Do you have a medical cause (Yes/No): ").lower()
if med == "yes":
    print ("You are allowed to take the exam.")
else:
    att = float(input("The days you werent in school (Except medical):"))
    if att>=13:
        print ("You can not take the exam because your attendance is poor" , att)
    else:
        print ("You can take the exam with your attendance" , att) 
