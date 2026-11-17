# Nested For loop Task
# ====================

# 1) Find the prime numbers from 1 to n
# =======================================

# n = int(input("Enter the number: "))

# while n <= 1:
#     print("Enter a number greater than 1")
#     n = int(input("Enter the number: "))
# for i in range(2, n + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# ========================================================================================================
# 2) Find the perfect numbers from 1 to 100
# =======================================

# for i in range(1, 101):
#     total = 0
#     for j in range(1, (i // 2) + 1):
#         if i % j == 0:
#             total += j
#     if total == i:
#         print(i)

# ========================================================================================================
# 3) Find the armstrong numbers from 1 to n
# =======================================

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     temp = i
#     total = 0
#     while temp > 0:
#         total += (temp % 10) ** len(str(i))
#         temp //= 10
#     if total == i:
#         print(i)
# ========================================================================================================
# 4) Find the palindrome numbers from 1 to 1000
# =======================================

# for i in range(1, 1001):
#     reverse = 0
#     temp = i
#     while temp > 0:  
#         reverse = (reverse * 10) + (temp % 10)
#         temp //= 10
#     if reverse == i:
#         print(i)
#     

#     or can use 
#     for _ in range(len(str(i))):
#         reverse = (reverse * 10) + (temp % 10)
#         temp //= 10

# ========================================================================================================
# 5) Find the strong numbers from 1 to 1000
# =======================================

# for i in range(1, 1001):0

#     temp = i
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         fact = 1
#         for j in range(1, digit + 1):
#             fact *= j
#         total += fact
#         temp //= 10
#     if total == i:
#         print(i)
# ========================================================================================================
# 6) Find the automorphic numbers from 1 to 1000
# =======================================

# for num in range(1, 1001):
#     length = len(str(num))
#     num_sqr = num ** 2
#     if num == (num_sqr % (10 ** length)):
#         print(num)
