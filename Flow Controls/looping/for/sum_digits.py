# write a program to return the sum of digits of the given number
num = input("Enter a number: ")
sum = 0
for i in num:
    sum += int(i)
print(f"The sum of digits of the number is {sum}")