# write a program to return the number of digits and alphabets from the given string
text = input("Enter the string: ")
alpha_count = digit_count = 0
for i in text:
    if i.isalpha():
        alpha_count += 1
    elif i.isdigit():
        digit_count += 1
print(f"Number of alphabets: {alpha_count} and number of digits: {digit_count}")
