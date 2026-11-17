# write a program to find the largest digit from the number
n = int(input("Enter a number: "))
largest = 0
for i in range(len(str(n))):
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print(largest)