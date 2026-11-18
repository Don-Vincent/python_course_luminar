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

# List Methods
item = []
item.append("Don")
item.append(10) # append() adds elements to the end of the list
print(item)

item.insert(1, "Vincent")
print(item)

item.insert(-1, 20) # using insert() we cannot add an elements to the end of a list so for that
# we use append()

item.count("Don")
# returns the count of the specified element in the list

item.index("10") 
# returns the index of the first occurance of the specified element in the list

item.remove("Vincent")
# removes the first occurance of the specified element from the list