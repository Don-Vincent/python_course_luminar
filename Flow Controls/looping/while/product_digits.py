# write a program to return the product of digits of a number

n = int(input("Enter the number: "))
product = 1
while n > 0:
    product *= n % 10
    n //= 10
print(f"The product of the digits of the number is: {product}")