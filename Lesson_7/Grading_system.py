print("Enter Marks for Obtained in 5 Subject")
sub1= int(input("enter Maths marks "))
sub2= int(input("enter Science marks "))
sub3= int(input("enter hindi marks "))
sub4= int(input("enter english marks "))
sub5= int(input("enter social studies marks "))
sum= sub1+sub2+sub3+sub4+sub5
average=sum/5
if 91 <= average <= 100:
    print("Your grade is A1" , average)
elif 81 <= average <= 90:
    print("Your grade is A2" , average)
elif 71 <= average <= 80:
    print("Your grade is B1" , average)
elif 61 <= average <= 70:
    print("Your grade is B2" , average)
elif 51 <= average <= 60:
    print("Your grade is C1" , average)
elif 41 <= average <= 50:
    print("Your grade is C2" , average)
elif 33 <= average <= 40:
    print("Your grade is D" , average)
elif 21 <= average <= 32:
    print("Your grade is E1" , average)
else:
    print("Your grade is E2" , average)