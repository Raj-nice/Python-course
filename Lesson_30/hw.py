class reverse:
    def __init__ (self):
        self.s = ""

    def reverse (self):
        self.s = input ("Enter String: ")
        self.s = self.s[::-1]

hi = reverse()
hi.reverse()
print("Reversed String: ", hi.s.lower())