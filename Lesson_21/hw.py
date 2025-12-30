num1 = int(input("Enter first value:"))
num2 = int(input("Enter second value:"))

if num1 == num2:
    print ("Ur so boring",num1*num2)
if num1 > num2:
    t = num1
    num1 = num2
    num2 = t
    t == num1 
    print ("Giving some extra work, not fun")
lst = []

for i in range (num1,num2 + 1):
    tt = t*t
    if t % 2 != 0:
        print ("Odd value", t*t)
    else:
        print ("Even value", t*t)
    lst.append(tt)
    t+=1
print (lst)


 