# write a program  to check whether the given number is perfect or not
def is_perfect(num):
  sum = 0
  for i in range(1, (num//2) + 1):
    if num % i == 0:
      sum += i
  print(f"Perfect" if num == sum else "Not perfect")

digit = int(input("Enter a number: "))
is_perfect(digit)
