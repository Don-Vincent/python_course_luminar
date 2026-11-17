"""
Pangram

It is a sentence, phrase or word that uses every letter of a given alphabet atleast once

"The quick brown fox jumps over the lazy dog"
"""
# text = input("Enter the text: ").lower()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     if i in text:
#         continue
#     print("This is not a pangram")
#     break
# else:
#     print("This is a pangram")


text = input("Enter the text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if i not in text:
        print("It's not a pangram")
        break
else:
    print("It is a pangram")