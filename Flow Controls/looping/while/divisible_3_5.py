# write a program to return the count of numbers divisible by 3 and 5 from 1 to 100

i = 1
count = 0
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        # print(i)
        count += 1
    i += 1
print(f"The count of numbers from 1 to 100 that are divisible by 3 and 5 is: {count}")
