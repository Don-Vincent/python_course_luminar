def is_armstrong(num):
  sum = 0
  temp = num
  count = len(str(num))
  while temp > 0:
    r = temp % 10
    sum += r ** count
    temp //= 10
  print(f"Armstrong" if sum == num else "Not armstrong")

num = int(input("Enter a number: "))
is_armstrong(num)