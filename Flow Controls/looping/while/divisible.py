# write a program to print numbers divisible by 3 from 1 to n

n = int(input("Enter a number: "))

i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1
