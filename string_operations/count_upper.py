# write a program to return the number of upper case characters in the given string

text = input("Enter a string: ")
count = 0
for i in text:
    if i.isupper():
        count += 1
print("Number of upper case characters:", count)