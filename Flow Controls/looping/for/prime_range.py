# write a program to print prime numbers from 5 to 100
for num in range(5, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
    