number = int(input("Enter a number: "))

odd = []

even = []

for i in range(1, number):
    if i % 2 == 0:
        even.append("" + str(i))
    else:
        odd.append("" + str(i))

fruits = ["Mango", "Orange", "Grapes", "Pineapple", "Banana", "Apple", "Watermelon", "Strawberry", "Papaya", "Kiwi", "Cherry", "Peach", "Apricot", "Avocado", "Cantaloupe", "Fig", "Guava", "Lemon", "Lime", "Blueberry"]

result = []
result = zip(odd, fruits)

print(list(result))