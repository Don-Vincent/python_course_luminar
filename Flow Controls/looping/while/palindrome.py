# program to check wheather the given number is palindrome or not

num = temp = int(input("Enter a number: "))
reverse = 0
while temp > 0:
    reverse = (reverse * 10) + temp % 10
    temp //= 10
if reverse == num:
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is a not a palindrome.")


# reverse = int((str(num))[::-1])
# if reverse == num:
#     print(f"The number {num} is a palindrome.")
# else:
#     print(f"The number {num} is a not a palindrome.")
