# #sum of nubers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


print(sum(numbers))
# or
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#get the largest number from the list

largest = 0
for i in numbers:
    if i > largest:
        largest = i
print(largest)
# or
print(max(numbers))

# get the smallest

smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)

# or
print(min(numbers))