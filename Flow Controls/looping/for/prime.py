# write a program to check the given number is prime or not
# 1 is not a prime number
# 2 is the only even prime number
# ==============================================
# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Not a prime.")
#     exit(0)
# if n == 2:
#     print("This is a prime number.")
#     exit(0)
# if n % 2 == 0:
#     print("Not a prime.")
#     exit(0)
# for i in range(3, int(n ** 0.5) + 1, 2):
#     if n % i == 0:
#         print("Not a prime.")
#         exit(0)
# print("This is a prime.")
# ===============================================
num = int(input("Enter a number: "))

while num <= 1:
    print("Enter a number above 1.")
    num = int(input("Enter a number: ")) 
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
