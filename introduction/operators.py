# # Arithmetic operators
# # ===============================================================
# # Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus (%), Exponentiation (**), Floor division (//)

# # Addition
# num_1 = 10
# num_2 = 5
# print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")

# # Subtraction
# num_1 = 10
# num_2 = 5
# diff = num_1 - num_2
# print(f"The difference between {num_1} and {num_2} is {diff}")

# # Multiplication
# num_1 = 10
# num_2 = 5
# product = num_1 * num_2
# print(f"The product of {num_1} and {num_2} is {product}")

# # Division
# num_1 = 10
# num_2 = 5
# quotient = num_1 / num_2
# print(f"The quotient of {num_1} and {num_2} is {quotient}")

# # Modulus
# num_1 = 10
# num_2 = 5
# remainder = num_1 % num_2
# print(f"The remainder of {num_1} divided by {num_2} is {remainder}")

# # Exponentiation
# num_1 = 10
# num_2 = 5
# power = num_1 ** num_2
# print(f"{num_1} raised to the power of {num_2} is {power}")

# # Floor division
# num_1 = 10
# num_2 = 5
# floor_division = num_1 // num_2
# print(f"The floor division of {num_1} by {num_2} is {floor_division}")

# Comparison Operators - result is always boolean(True/False)
# ============================================================================================
# > : Greater than
# < : Less Than
# <= : Less than or equal to
# >= : Greater than or equal to
# == : equals to
# != : Not equal to

# num_1 = 10
# num_2 = 20

# print(num_1 < num_2)  # True
# print(num_1 > num_2)  # False
# print(num_1 <= num_2)  # True
# print(num_1 >= num_2)  # False
# print(num_1 == num_2)  # False
# print(num_1 != num_2)  # True

# Concatenation
# ==================================
# joinin two stings using the '+' operator is called concatenation

# fname = "Don"
# lname = " Vincent"
# print(fname + lname)  # Don Vincent
# # Also

# print(fname * 4)  # DonDonDonDon
# ==========================================
# print(True > False)  # which is 1 > 0, output will be True
# print('a' > 'A')  # which compares the ASCII values of character capital letters start from A=65 and smal letters start from a = 97
# # therefore the result would be True
# print("abc" > "acb")
# print("abc" < "abd")


# Assignment operator
# =====================================================================
# =     num = 10
# +=    num += 10
# -=    num -= 10
# /=    num /= 10
# *=    num *= 10
# %=    num %= 10
# **=   num **= 10
# //=   num //= 10


#Membership operator
# =====================================================================
# in : returns True if a sequence with the specified value is present in the string
# not in : returns True if a sequence with the specified value is not present in the string

# example:

# name = "Don Vincent"
# print("Don" in name)  # True
# print("john" not in name)  # True   
# print("incent" not in name)  # False
