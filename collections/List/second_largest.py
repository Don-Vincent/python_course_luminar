numbers = [12, 8, 3, 5, 6, 9, 10, 11, 1]



numbers.sort()
print(numbers[-2])

# or


numbers = [8, 12, 3, 5, 6, 9, 10, 11, 1]

largest = second_largest = float('-inf')

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest: # if we want secan largest distinct value put condition elif largest > i > second_largest:
        second_largest = i

print(second_largest)