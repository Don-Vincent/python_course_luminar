# program to check whether the given number is armstrong or not
"""
Armstrong number is a number that equals the sum of its own digits,
where each digit is raised to the power of the total number of digits

• (153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
• (370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370)
"""

num = temp = int(input("Enter a number: "))
sum = 0
count = len(str(num))
while temp > 0:
    r = temp % 10
    sum += r ** count
    temp //= 10
if sum == num:
    print(f"{num} is an amstrong number.")
else:
    print(f"{num} is not an amstrong number.")


# num = int(input("Enter a number: "))
# temp = str(num)
# count = len(temp)
# total = sum(int(digit) ** count for digit in temp)
# if total == num:
#     print(f"{num} is an armstrong number.")
# else:
#     print(f"{num} is not an amstrong number.")
