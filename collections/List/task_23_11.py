numbers  = [2, 7, 11, 15, 3, 5, 6]
target = 9
# return the index of two numbers from the list of their sum equals the target




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