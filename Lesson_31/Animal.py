from abc import ABC, abstractclassmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print ("I am Human, I can walk or run")

class Snake(Animal):
    
    def move(self):
        print ("I am Snake, I can crawl")

class Dog(Animal):

    def move(self):
        print ("I am Dog,   I can bark")

class Lion(Animal):

    def move(self):
        print ("I am Lion,  I can roar")

R = Human()
R.move()

K = Snake()
K.move()

G = Dog()
G.move()

L = Lion()
L.move()
