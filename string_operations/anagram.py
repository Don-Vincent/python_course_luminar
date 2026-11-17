"""
a word or phrase formed by rearranging the letters of another word or phrase,
using all the original as the same number as in the original
"""
word_1 = "silent"
word_2 = "listen"
if len(word_1) == len(word_2):
    for i in word_1:
        if word_1.count(i) != word_2.count(i):
            print("Not an anagram")
            break
    else:
        print("Anagram")
else:
    print("Not an Anagram")
