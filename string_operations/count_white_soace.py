# write a program to count the total number of white spaces in the given string
sentence = input("Enter a string: ")
count = 0
for i in sentence:
    if i == " ":
        count += 1
print(f"The total number of white spaces in the string is {count}")