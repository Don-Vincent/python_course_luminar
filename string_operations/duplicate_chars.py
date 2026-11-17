# write a program to retutrn the duplicate characters in the given string
text = input("Enter your text: ")
duplicate = ""
for i in text:
    if text.count(i) > 1 and i not in duplicate:
        duplicate += i
        print(i, end=" ")
#       duplicate += i + " " 
# print(duplicate)
