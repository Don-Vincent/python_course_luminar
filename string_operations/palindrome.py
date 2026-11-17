# program to check the string is palindrome
"""
a word, phrase, number that reads the same backwards as it does forward
"""
text = input("Enter the text: ")
print("Palindrome" if text == text[::-1] else "Not Palindrome")

print(reversed(text))
