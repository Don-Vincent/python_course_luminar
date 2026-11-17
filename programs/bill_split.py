# Program to read the total amount of a bill and the number of diners from the user and prin what each persons split

bill_amnt = int(input("Enter the total bill amount: "))
num_diners = int(input("Enter the number of diners: "))

split = bill_amnt / num_diners
print("Each person must pay: ", split)
