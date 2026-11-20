#  return the largesrt word from the string given
text = "python is a programming language"

print(max(text.split(), key = len))

# or

# longest = ""
# arr = text.split()
# for w in arr:
#     if len(w) > len(longest):
#         longest = w
# print(longest)