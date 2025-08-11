text = input("Enter a string ")
reversed = ""
for i in text:
    reversed=i+reversed
print ("Reveresed Text: ",reversed)
if reversed == text:
    print ("This is a Pallindrome")
else:
    print ("This is not a pallindrome")