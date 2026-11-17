"""
Ask user for age. If age is 18 or above, print they can vote.
if age is 17, print "You can learn to drive."
if age is 16 print "You can buy a lottery ticket."
if age is inder 16 print, "You can go Trick - or - Treating"
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age == 17:
    print("You can learn how to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go trick or treating.")
