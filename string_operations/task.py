text = "aaabbbbccd" # o/p -> "a3b4c2d1"
temp = ""
for i in text:
    if i not in temp:
        temp += i + str(text.count(i))
print(temp)