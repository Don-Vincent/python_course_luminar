"""
Spy number
a positive integer where the sum of digits equals to the product of its digits

"""
num = input("Enter a number: ")
sum = 0
product = 1
for i in num:
    sum += int(i)
    product *= int(i)
print(f"{num} is a spy number" if sum == product else f"{num} is not a spy number.")