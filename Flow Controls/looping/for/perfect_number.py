"""
A perfect number is a positive integer that equals the sum of its positive proper divisors
(all divisors excluding  the number itself)
example:
6 = 1+2+3
28 = 1+2+4+7+14
"""
n = int(input("Enter a number: "))

total = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        total += i
# if total == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")
print(f"the {n} is perfect" if n == total else f" the {n} not perfect") # this is called ternary operator

# another example 
# result = "even" if number % 2 == 0 else "odd"