# program to count the number of consonants

name = input("Enter your name: ")
vowels = "aeiou"
count = 0
for i in name.lower():
    if i not in vowels:
        count += 1
print(f"There are {count} consonants in your name.")