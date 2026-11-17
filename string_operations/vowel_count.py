# write a program to return the number of vowels in the given string
name = input("Enter your name: ")
vowels = "aeiou"
count = 0

for i in name.lower():
    if i in vowels:
        count +=1
print(f"There are {count} vowels in your name.")