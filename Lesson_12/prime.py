start = int(input("Enter the starting number: "))

end = int(input("Enter the ending number: "))

print('Prime numbers between : ',start, 'and',end)

num=start

while num <= end:

    if num >1:

        is_prime=True

    for i in range(2, num):

        if num % i == 0: # If divisible by any number other than 1 and itself

            is_prime = False

            break

    if is_prime:

        print(num)

    num += 1
