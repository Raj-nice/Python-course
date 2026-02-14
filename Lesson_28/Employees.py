class Emboyees:

    def __init__ (self):
        print ("Employee created")
    def __del__ (self):
        print ("Destructor called")

def Create_obj():
    print("Making Object...")
    obj = Emboyees()
    print ("Function end...")
    return obj
print ("Calling Create_obj() function ...")
obj = Create_obj()
print ("Program ends")

