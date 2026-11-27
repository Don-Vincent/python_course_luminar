# wap to retutn len of each word in a string
text = "python is a programming language"

def word_len(text):
    words = text.split()
    len_list = {}
    for i in words:
        len_list[i] = len(i)
    return len_list
print(word_len(text))

