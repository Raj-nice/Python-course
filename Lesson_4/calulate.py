user=int(input("Enter the amount you want to withdraw "))
note1= user//100
note2= (user%100)//50
note3= ((user%100)%50)//20
note4= (((user%100)%50)%20)//10
print("notes of 100 rupee" , note1)
print("notes of 50 rupee" , note2)
print("notes of 20 rupee" , note3)
print("notes of 10 rupee" , note4)