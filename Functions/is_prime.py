# write a program to check whether the number is prime of not
def is_prime(num:int):
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
for _ in range(5):
    number = int(input("Enter a number: "))
    while number <= 1:
        number = int(input("Enter a number: "))
    is_prime(number)
