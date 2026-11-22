
# 1) Find the prime numbers from 1 to n
# =============================================================

# def prime(num):
#     prime_list = []
#     for i in range(2, num + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             prime_list.append(i)
#     return prime_list

# n = int(input("Enter a number: "))
# print(prime(n))

# =============================================================
# 2) Find the perfect numbers from 1 to 100
# =============================================================

# def find_perfect():
#     list_perfect = []
#     for i in range(1, 101):
#         total = 0
#         for j in range(1, i // 2 + 1):
#             if i % j == 0:
#                 total += j
#         if total == i:
#             list_perfect.append(i)
#     return list_perfect
# print(find_perfect())
# =============================================================
# 3) Find the armstrong numbers from 1 to n
# =============================================================

# def find_armstrong(n):
#     armstrong_list = []
#     for i in range(1, n + 1):
#         temp = i
#         total = 0
#         digits = len(str(i))
#         while temp > 0:
#             total += (temp % 10) ** digits
#             temp //= 10
#         if total == i:
#             armstrong_list.append(i)
#     return armstrong_list
# n = int(input("Enter a number: "))
# print(find_armstrong(n))
# =============================================================
# 4) Find the palindrome numbers from 1 to 1000
# =============================================================

# def palindrome():
#     return [x for x in range(1, 1001) if str(x) == str(x)[::-1]]
# print(palindrome())

# =============================================================
# 5) Find the strong numbers from 1 to 1000
# =============================================================

# def strong():
#     strong_list = []
#     def fact(n):
#         t = 1
#         for x in range(1, n + 1):
#             t *= x
#         return t
#     for i in range(1, 1001):
#         temp = i
#         total = 0
#         while temp > 0:
#             total += fact(temp % 10)
#             temp //= 10
#         if total == i:
#             strong_list.append(i)
#     return strong_list
# print(strong())

# or

# def strong():
#     strong_list = []
#     def fact(n):
#         t = 1
#         for x in range(1, n + 1):
#             t *= x
#         return t
#     factorials = [fact(x) for x in range(10)]
#     for i in range(1, 1001):
#         temp = i
#         total = 0
#         while temp > 0:
#             total += factorials[temp % 10]
#             temp //= 10
#         if total == i:
#             strong_list.append(i)
#     return strong_list
# print(strong())

# =============================================================
# 6) Find the automorphic numbers from 1 to 1000
# =============================================================

# def automorphic():
# return [x for x in range(1, 1001) if str(x ** 2).endswith(str(x))]
#     or
# return [x for x in range(1, 1001) if x ** 2 % (10 ** len(str(x))) == x]

# print(automorphic())

# =============================================================
# 7)Remove duplicate elements
#    [1, 2, 2, 3, 4, 4, 5, 1]
# =============================================================

# nums = [1, 2, 2, 3, 4, 4, 5, 1]

# print (list(set(nums)))

# or

# unique = []
# for i in nums:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# =============================================================
# 8)Separate even and odd numbers into two different list
#   [10, 15, 20, 25, 30, 35]
# =============================================================

# nums = [10, 15, 20, 25, 30, 35]
# odd = []
# even = []
# for i in nums:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Odd: {odd}\nEven: {even}")

# =============================================================
# 9)Find common elements between two lists
#   List 1:
#     [1, 2, 3, 4]
#  List 2:
#     [3, 4, 5, 6]
# =============================================================

# list_1 = [1, 2, 3, 4]
# list_2 = [3, 4, 5, 6]

# print([x for x in list_1 if x in list_2])

# =============================================================
# 10)Remove all even numbers
#    [1, 2, 3, 4, 5, 6]
# =============================================================

# nums = [1, 2, 3, 4, 5, 6]
# print([x for x in nums if x % 2 != 0])


# =============================================================
# 11)Find sum of all elements
#     [5, 10, 15, 20]
# =============================================================

# nums = [5, 10, 15, 20]
# print(sum(nums))

# =============================================================
# 12)Find the shortest string in the list
#   List:
#      ["python", "js", "java", "c"]
# =============================================================

# words = ["python", "js", "java", "c"]
# print(min(words, key = len))

# =============================================================
# 13)Convert all strings to uppercase
# List:
#     ["hello", "world", "python"]
# =============================================================

# words = ["hello", "world", "python"]
# words = [x.upper() for x in words]
# print(words)

# =============================================================
# 14)Find all strings that end with 'a'
#  List:
#    ["data", "code", "java", "python", "scala"]

# words = ["data", "code", "java", "python", "scala"]
# ends_a = [x for x in words if x.endswith("a")]
# print(ends_a)
