user_input = str(input("Enter a Phrase: "))
# The split() method splits a string into a list
text = user_input.split()
print(text)
a = " "
for i in text:
    #pick the first letter of the word and make it uppercase
    a = a+str(i[0]).upper()
print(a)