# check the given string is palindrome or not

text = "malayalam"
new = ""
# for i in reversed(text):
#     new += i
# print(new)

for i in range(len(text) - 1, -1, -1):
    new += text[i]
print("Palindrome" if new == text else "Not a Palindrome")
