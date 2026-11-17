# write a program to print nunbers divisible by 2 and 5 from 100 to 10

i = 100

while i >= 10:
    if i % 2 == 0 and i % 5 == 0:
        print(i)
    i -= 1
