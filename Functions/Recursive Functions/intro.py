"""
A recursive function in Python is a function that calls itself during its execution 
to solve a problem. Instead of solving a large task all at once, recursion breaks it 
down into smaller, identical subproblems until it reaches a simple stopping point.

Two Essential Parts

Every working recursive function needs two core components:
• Base Case. This is the stopping condition that ends the recursion. Without a base case, 
the function calls itself forever and triggers a RecursionError.
• Recursive Case. This is the part where the function calls itself with a smaller or 
modified input. Each call moves the problem closer to the base case.
"""


# Factorial of a number
# ===========================
# Normal
def factorial_1(num):
  fact = 1
  for i in range(1, num + 1):
    fact *= i
  return fact


# Recursive
def factorial_2(num):
  if num == 0 or num == 1:
    return 1
  return num * factorial_2(num - 1)


num = int(input("Enter a number: "))
print(factorial_1(num))
print(factorial_2(num))