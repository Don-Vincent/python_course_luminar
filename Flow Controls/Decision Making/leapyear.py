"""
Program to check weather a number is leap year or not

two types of years 
& Century year - divisible by 400
& Non Century year - divisible by 4 and not by 100

"""

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
