# write a program to get the factors of the number given by the user

num = int(input("Enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1

# arr = []
# arr = [x for x in range (1, num + 1) if num % x == 0]
# print(arr)