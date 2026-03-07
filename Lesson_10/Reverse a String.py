text = input("Enter a string ")
reversed = ""
for i in text:
    reversed=i+reversed
if text == reversed:
    print ("Your name is the same! ")
else:
    print ("Reveresed Text: ",reversed)