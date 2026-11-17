# Program to take the initial number of slices of pizza and how many many slices they eat and figure out how many left

total_slice = int(input("Enter number of slices of pizza you started with: "))
slice_eaten = int(input("Enter the number of slices you have eaten: "))

remaining_slice = total_slice - slice_eaten
print("The remaining number of slices: ", remaining_slice)

