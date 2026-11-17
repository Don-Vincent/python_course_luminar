# write a program to return the number of digits in a number

n = int(input("Enter a number: "))
count = 0
if n == 0:
    print(1)
    exit(0)
while n > 0:
    count += 1
    n //= 10
print(count)

# n = input("Enter the number")
# print(len(n))