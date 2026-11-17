# strong number is a positive integer whose sum of the factorials of its individual digits equals the number itself

temp = num = int(input("Enter a number: "))
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    temp //= 10
print(f"Strong" if total == num else f"Not Strong")

