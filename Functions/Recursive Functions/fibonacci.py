"""
fibonacci numbers form a sequence where each number is the sum of the two 
numbers that precedes it, starting with zero and one
0 1 1 2 3 5 8 13 21 34....
"""
# method 1 to print fibonacci series less than a number
# a = 0
# b = 1
# n = 40
# while a <= n:
#   print(a)
#   a, b = b, a + b

# method 2 to print first n fibonacci series
# n = 10
# count = 0
# a, b = 0, 1
# while count < n:
#   print(a)
#   count += 1
#   a, b = b, a + b

# method 3 recursive
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)
for i in range(10):
  print(fibonacci(i))