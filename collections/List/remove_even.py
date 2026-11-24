numbers = [5, 3, 6, 8, 9, 10, 13, 12, 11]

def remove_even1(numbers):
    for i in numbers.copy(): ##################################################IMPORTANT
        if i % 2 == 0:
            numbers.remove(i)
    return numbers

def remove_even2(numbers):
    return [x for x in numbers if x % 2 != 0]

print(remove_even1(numbers))
print(remove_even2(numbers))