number = int(input("Enter a decimal number to convert to binary:"))
i = 1
h = 0
while i<number:
    i*=2
    h+=1
i/=2
for h in range (0,h):
    if i<=number:
        number-=i
        i/=2
        print(1, end='')
    else:
        i/=2
        print(0,end='')


