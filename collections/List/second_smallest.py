numbers = [8, 12, 3, 5, 6, 9, 10, 11, 1]

# numbers.sort()
# print(numbers[1])

# or


def second_smallest(numbers):
    smallest = sec_smallest = float('inf')
    for i in numbers:
        if i < smallest:
            sec_smallest = smallest
            smallest = i
        elif i < sec_smallest: # if we require distinct second smallest value then give condition elif smallest < i < sec_smallest:
            sec_smallest = i
    return sec_smallest
print(second_smallest(numbers))