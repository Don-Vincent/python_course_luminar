# check whether the given number is automorphic or not
"""
a natural number whose square ends with the digits of the number itself

5 >>>>> 5 ^ 2 = 25
6 >>>>> 6 ^ 2 = 36
25 >>>> 25 ^ 2 = 625
"""
num = int(input("Enter a number: "))
num_sqr = num ** 2
temp = num_sqr % (10 ** len(str(num)))
print("Automorphic" if temp == num else "Not automorphic")