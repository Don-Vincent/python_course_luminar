numbers  = [2, 7, 11, 15, 5]
target = 9
# return the index of two numbers from the list of their sum equals the target


# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return [i, j]
#     print([])   
# print(two_sum(numbers, target))



# def two_sum(numbers, target):

#     for i in range(len(numbers)):
#         remaining = target - numbers[i]
#         if remaining in numbers[i + 1:]:
#             return i, numbers[i + 1:].index(remaining) + i + 1

# print(two_sum(numbers, target))


# Using dictionary

# if you want all index pairs achieving target sum
# def two_sum(numbers, target):
#     diff = {}
#     result = []
#     for i in range(len(numbers)):
#         remaining = target - numbers[i]
#         if remaining in diff:
#             result.append((diff[remaining], i))
#         diff[numbers[i]] = i
#     return result
# print(two_sum(numbers, target))

# else

# def two_sum(numbers, target):
#     diff = {}
#     for i in range(len(numbers)):
#         remaining = target - numbers[i]
#         if remaining in diff:
#             return diff[remaining], i
#         diff[numbers[i]] = i
# print(two_sum(numbers, target))



# For three sum targets 

# numbers  = [2, 7, 11, 15, 5]
# target = 24
# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             for k in range(j + 1, len(numbers)):
#                 if numbers[i] + numbers[j] + numbers[k] == target:
#                     return [i, j, k]
#     print([])   
# print(two_sum(numbers, target))



def two_sum(numbers, target):
    n = len(numbers)
    for i in range(n - 2):
        rem = target - numbers[i]
        seen = {}
        for j in range(i + 1, n):
            needed = rem - numbers[j]
            if needed in seen:
                return [i, seen[needed], j]
            seen[numbers[j]] = j
    return []
numbers  = [2, 7, 11, 15, 5]
target = 24
print(two_sum(numbers, target))