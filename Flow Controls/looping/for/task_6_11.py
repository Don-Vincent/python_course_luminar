# check the prime numbers from  1 to n
# ========================================

# n = int(input("Enter a number: "))
# while n <= 1:
#     print("Enter a number above 1.")
#     n = int(input("Enter a number: ")) 
# for i in range(2, n + 1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# ======================================================================================================
# check the prime numbers from 100 to 10
# ========================================

# for i in range(100, 9, -1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# ======================================================================================================

# get the  first 10 prime numbers from 1 to n
# ========================================

# n = int(input("Enter a number: "))
# count = 0
# while n <= 1:
#     print("Enter a number above 1.")
#     n = int(input("Enter a number: ")) 
# for i in range(2, n + 1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         count += 1
#         print(i)
#         if count == 10:
#             break
# ======================================================================================================

# get the prime factors of the number enter by user
# ========================================

# n = int(input("Enter a number: "))
# for i in range(2, n + 1):
#     if n % i == 0:
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# ======================================================================================================


# wap to print the characters of a string in even positions. >>>      name= "python"    o/p = y h n
# ========================================

# name = input("Enter your name: ")
# while len(name) < 2:
#     name = input("There are no characters at even position, Enter a name with length greater than or equal to 2")
# for i in range(1, len(name), 2):
#     print(name[i])

# ======================================================================================================

# wap to print sum of even and odd indexed digits in a given number
# ========================================

# number = int(input("Enter a number: "))
# odd_sum = 0
# even_sum = 0
# for i in str(number):
#     if str(number).index(i) % 2 == 0:
#         even_sum += int(i)
#     else:
#         odd_sum += int(i)
# print(f"odd sum: {odd_sum} and even sum: {even_sum}")
# ======================================================================================================

#Write a Python program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number, 
# and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz"
# 1,2,"Fizz",4,"Buzz",....,13,14,"FIzzbuzz"..............
# ==========================================
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# =========================================================================================================
