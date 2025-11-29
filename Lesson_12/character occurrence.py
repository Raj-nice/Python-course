word = input("Enter a word:")
i = 0
while i < len(word):
    count = 0
    for char in word:
        if word[i].lower() == char.lower():
            count +=1
    print (word[i], "occurs" , count , "times")

    i +=1