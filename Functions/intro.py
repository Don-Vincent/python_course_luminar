# Functions
# ====================
# Each function has a block of code that performs a specific task.
# The function is reusable(it can be called again and again)
# example:
# print()
# len()
# ======================================================================
# def is used to define a function

def sample(): # function header
    print("Hello") # function body
sample() # function call

# function body
# ===================
# The block of code inside a function that gets executed each time a function is called


# function call
# ===================
# The statement of code that calls a function



"""
positional arguments
====================
average(10, 20, 30) -> positional arguments : arguments passed to thw fucntion based on the position of the parameters

keyword arguments
====================
average(num_1 = 10, num_3 = 30, num_2 = 20) _> keyword arguments : arguments passed using the parameter names, order dont matter

variable arguments
====================
def addition(*args): # variable number of arguments
    body

addition(10, 20)
addition(10, 20, 30)

varible number of arguments can be used


Default argument
====================

def details(name, place = "Kochi"):
    print(place, name)

gives a default value to the parameter.
even if we dont give a value as the argumnet the parameter takes the default value
if we pass a value as argument to the variable the passed value will override the default value

"""
# def addition(*args):
#     total = 0
#     for i in args:
#         total += i
#     print(total)
# addition(20, 30, 40)
# addition(20, 30)

