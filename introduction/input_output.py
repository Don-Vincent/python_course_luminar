# input/output

# the input() function is used to take input from the user. The input() function takes a string as input.
name = input("Enter your name: ")
# the input() function takes a string as input. The int() function is used to convert the string to an integer.
age = int(input("Enter your age: "))
print(name)
print(f"Hello {name}, you are {age} years old.")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("The sum of", n1, "and", n2, "is", n1 + n2)

a1 = input("Enter the first number: ")
a2 = input("Enter the second number: ")
# type conversion, also can use float() to convert to float and str() to convert to string
sum = int(a1) + int(a2)
print(f"The sum of {a1} and {a2} is {sum}")
