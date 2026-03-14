from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self,x):
        print("Passed value:", x)

    @abstractmethod
    def task(self):
        print ("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

test = test_class()
test.task()
test.print(100)