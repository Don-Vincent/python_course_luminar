# wap to return non prime numbers from the list given

numbers = [1, 4, 2, 5, 6, 11, 23, 20, 15]
non_prime = []
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                non_prime.append(num)
                break
    else:
        non_prime.append(num)    
print(non_prime)