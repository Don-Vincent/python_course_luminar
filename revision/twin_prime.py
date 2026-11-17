# write a program to return the twin prime numbers from 1 to 100
# A twin prime is a pair of prime numbers that have a difference of exactly 2 (such as 11 and 13)
previous = 2
count = 0
i = 2
while count < 10:
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    if (i - previous) == 2:
      print(f"{previous, i}")
      count += 1
    previous = i
  i += 1

# or we can do

# while(True):

#   ------
#   if count == 10:
#     break
#   --------