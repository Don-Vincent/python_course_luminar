# write a program to returnthe total number of characters in a string entered by the user
string = input("Enter a string: ")
count = 0
for _ in string:
    count += 1
print(f"The total number of characters in the string is {count}")

