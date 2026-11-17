# String Operations
"""
        0123456
name = "sukumar"
strings are collection of characters. they are immutable.(letters, numbers, symbols, etc)
duplicate characters are allowed in strings. 
index positioning (zero based index positioning) is used to access the characters in a string.
string is iterable. we can iterate through the string using for loop.(like range, list, tuple, etc)
"""

# Slicing
# ===========
name = "hellopython"
print(name[4])

print(name[:5])
# output: hello

print(name[6:])
# output: python

print(name[-1]) # negative indexing
#output: n

print(name[3:8]) # start(included): end(excluded)
# output: lo py

print(name[::-1]) # reverse the string
# output: nohtyp olleh

print(name[:5] + name[5:][::-1])
fword = name[:5]
lword = name[5:]
print(fword + lword[::-1])
# output: hellonohtyp


print(name[0:3] + name[3:9][::-1] + name[9:])
# output:helhtypolon

# =====================================
# String Methods
# ================
# variab_name.method_name()
name = "hellopython"

print(name.capitalize())  #-------> name[0].upper() + name[1:].lower()
# Hellopython
# retunrns first character of the string in uppercase and rest of the characters in lowercase

print(name.upper())
# HELLOPYTHON

print(name.lower())
# hellopython

print(name.count("l")) #return the number of occurrences of the given character in the string
# output: 2

name = "Hello Python"
print(name.swapcase()) # return the string with all uppercase characters in lowercase and all lowercase characters in uppercase
# output: hELLO pYTHON

name = "Hello Python"
print(name.index("P")) # return the index position of the first occurance of the given character in the string
# output: 6

name = "hello python"
print(name.title()) # return the string with first character of each word in uppercase and rest of the characters in lowercase
# output: Hello Python

name = "Hello Python"
print(name.find("P"))
# returns the first index if present else it rreturns -1, if the given character is not present

print(name.islower()) 
print(name.isupper())
print(name.isalpha()) # return true if alphabets
print(name.isalnum()) # return true if a colllection of alphabets and/or numbers
print(name.isdigit()) # returns true if its a digit
print(name.isspace()) # returns true if the string is a white space