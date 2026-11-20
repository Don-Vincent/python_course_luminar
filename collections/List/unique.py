# write a program to return unique characters from the string given

word = "hellopython" # >> ["e", "p", "y", "t", "n"]
unique = []
for i in word:
    if word.count(i) == 1:
        unique.append(i)
print(unique)

# or

uni = [ch for ch in word if word.count(ch) == 1]
print(uni)