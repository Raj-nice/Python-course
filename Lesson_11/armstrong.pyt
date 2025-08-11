n = int(input("Enter a number:"))
ord = len(str(n))
sum = 0
tem = n
while tem > 0:
    dig = tem % 10
    sum += dig ** ord
    tem //=10
if n == sum:
    print ("Armstrong number!!")
else:
    print ("TRY AGAIN")