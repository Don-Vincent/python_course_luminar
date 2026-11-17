# write a program to find the smallest digit from the number
n = int(input("Enter a number: "))
smallest = 9
for i in range(len(str(n))):
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print(smallest)
