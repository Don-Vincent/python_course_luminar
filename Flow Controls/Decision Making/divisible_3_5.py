# to Check a number is divisible by both 5 and 3 or not

num = int(input("Enter the number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"The number {num} is divisible by both 3 and 5.")
else:
    print(f"Not divisible by both 3 and 5.")

"""
Condition 1     condition 2     AND     OR   
TRUE            TRUE            TRUE    TRUE
TRUE            FALSE           FALSE   TRUE
FALSE           TRUE            FALSE   TRUE
FALSE           FALSE           FALSE   FALSE


"""
