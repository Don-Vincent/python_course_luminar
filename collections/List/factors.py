# define a function which returns factors of the number entered by the user

def factors(num):
    fact = []
    for i in range(1, num + 1):
        if num % i == 0:
            fact.append(i)
    return(fact)
n = int(input("Enter a number: "))
print(factors(n))