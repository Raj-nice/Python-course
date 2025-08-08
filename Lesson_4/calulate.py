user=int(input("Enter the amount you want to withdraw "))
note1= user//500
note2= (user%500)//200
note3= ((user%500)%200)//100
note4= (((user%500)%200)%100)//50
note5= ((((user%500)%200)%100)%50)//20
note6= (((((user%500)%200)%100)%50)%20)//10
note7= ((((((user%500)%200)%100)%50)%20)%10)//5
note8= (((((((user%500)%200)%100)%50)%20)%10)%5)//2
note9= ((((((((user%500)%200)%100)%50)%20)%10)%5)%2)//1
print("notes of 500 rupee" , note1)
print("notes of 200 rupee" , note2)
print("notes of 100 rupee" , note3)
print("notes of 50 rupee" , note4)
print("notes of 20 rupee" , note5)
print("notes of 10 rupee" , note6)
print("coins of 5 rupee" , note7)
print("coins of 2 rupee" , note8)
print("coins of 1 rupee" , note9)
