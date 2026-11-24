"""
Collections
============
To assign more than one values in a single variable


Types of Collections
====================
* List
* Tuple
* Set
* Dictionary


List
======
items = []   #list data type
or
items = list()
"""
item = ["python", 10, 7.5, True, "python", []]

# Oreder of elements are preserved
# It allows duplicate elements
# Each elements has its index position(zero based index)
# Hetrogeneous(allows values of all data types)
# List is mutable
# iterable

# List Methods
# item = []
# item.append("Don")
# item.append(10) # append() adds elements to the end of the list
# print(item)

# item.insert(1, "Vincent")
# print(item)

# item.insert(-1, 20) # using insert() we cannot add an elements to the end of a list so for that
# # we use append()

# item.count("Don")
# # returns the count of the specified element in the list

# item.index("10") 
# # returns the index of the first occurance of the specified element in the list

# item.remove("Vincent")
# # removes the first occurance of the specified element from the list

# numbers = [1, 5, 3, 6, 3, 1]


# print(numbers.pop())
# print(numbers)
# # pop method removes the last element from the list and returns the removed value to the user

# print(numbers.pop(4))
# # if we give an index position as argument to the pop method, it removes the value at that index position and 
# # returns it to the user


numbers_1 = [1, 5, 3, 6, 3, 1]
numbers_2 = [10, 20, 9, 5]
numbers_1.extend(numbers_2) # appends the second list to the first one in position
print(numbers_1)
# [1, 5, 3, 6, 3, 1, 10, 20, 9, 5]

numbers_1.sort()
print(numbers_1)
# sort method sorts the list in position permanently in adcending order
# [1, 1, 3, 3, 5, 5, 6, 9, 10, 20]

numbers_1.sort(reverse = True) # sorts in descending order
print(numbers_1)
# [20, 10, 9, 6, 5, 5, 3, 3, 1, 1]

numbers_1.reverse()
print(numbers_1) # in position reverse
# [20, 10, 9, 6, 5, 5, 3, 3, 1, 1]

numbers_1.clear()
print(numbers_1)
# empty list []