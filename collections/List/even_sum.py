# wap to get list of numbers from 1 to 10

arr = [x for x in range(1, 11)]
# print(arr)

# or

# arr = list(range(1, 11))
# print(arr)

# arr = []
# for i in range(1, 11):
#     arr.append(i)
# print(arr)
tot = 0
for i in arr:
    if i % 2 == 0:
        tot += i
print(tot)

total = sum(x for x in arr if x % 2 == 0)
print(total)