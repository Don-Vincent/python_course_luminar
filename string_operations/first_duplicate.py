# # write a program to print the first duplicate character from the string given

# text = "programming"
# for i in text:
#     if text.count(i) > 1:
#         print(i)
#         break

"""
write a program that takes a string from the user "hellopython"
Find the first occurance of the character 'p' in the string
swap all the characters before this first occurance of 'p'
Leave the rest of the string unchanged\
if "p" is not present in the given string return entire string in reverse
"""
text  = "hellopython"

if "p" in text:
    p_index = text.index("p")
    print(text[:p_index][::-1] + text[p_index:])
else:
    print(text[::-1])
