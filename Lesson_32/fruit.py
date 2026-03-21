import random

class FruitQuiz:

    def __init__(self):

        self= {"apple" : "red", "orange" : "orange", "watermelon" : "green", "banana" : "yellow"}

    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruit.items()))
            user_answer = input()

            if(user_answer.lower()== color):
                print("Correct answer")
                i+=1

            else:
                print ("Wrong answer")
                j+=1

            option = int(input("Enter 0 , if you want to play again otherwise enter 1: "))
            if(option):
                print ("Your score is", )
                break

    print("Welcome to fruit quiz: ")
fq = FruitQuiz()
fq.quiz()