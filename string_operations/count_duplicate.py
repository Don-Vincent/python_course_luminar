# program to count the number of duplicate characters

text = input("Enter the text: ")
count = 0
duplicate = ""
for i in text:
    if text.count(i) > 1 and i not in duplicate:
        count += 1
        duplicate += i
print(count)

# from collections import Counter
# counts = Counter(text)