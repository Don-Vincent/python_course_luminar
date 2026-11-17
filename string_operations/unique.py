# write a program to return unique characters in a string
text = input("Enter the text: ")
for i in text:
    if text.count(i) == 1:
        print(i, end = "")