# write a program to return the character count from the string entered by the user
def char_count(text):
  new = "" 
  for i in text:
    if i not in new:
      print(i,":", text.count(i))
      new += i
line = input("Enter a string: ")
char_count(line)