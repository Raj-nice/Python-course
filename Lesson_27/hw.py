class Dog:


    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

goldy = Dog("brown", "golden retriever")
max = Dog("black", "poodle")

print("Goldy is a {} {}.".format(goldy.color, goldy.breed))
print("Max is a {} {}.".format(max.color, max.breed))


