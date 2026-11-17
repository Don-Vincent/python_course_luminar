# Harshad number
# it is a number that is divisible by its sum of digits

n = temp = int(input("Enter a number: "))
total = 0
for i in range(len(str(n))):
    total += n % 10
    n //= 10
print("Harshad" if temp % total == 0 else "not a harshad")