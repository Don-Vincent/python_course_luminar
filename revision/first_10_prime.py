# program to print first 10 prime numbers
num = 2
count = 1
while count <= 10:
  for i in range(2, num):
    if num % i == 0:
      break
  else:
    print(num)
    count += 1
  num += 1  