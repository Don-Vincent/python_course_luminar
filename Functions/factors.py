# wap to return the factors of a number given by the user
def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
factors(10)

"""
average(10, 20, 30) -> positional arguments : arguments passed to thw fucntion based on the position of the parameters
average(num_1 = 10, num_3 = 30, num_2 = 20) _> keyword arguments : arguments passed using the parameter names, order dont matter
"""