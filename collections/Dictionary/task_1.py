# wap to return the count of each characters from a string
name = "hello"

# from collections import Counter
# counts = Counter(name)
# print(counts)

def char_count(name):
    ccount = {}
    for i in name:
        ccount[i] = name.count(i)
    return ccount
print(char_count(name))