# Set
# ======
# can be defined set()
# Duplicates are not allowed
# order is not preserved
# there are no indexing 
# Iterable but still no indexing and order preserving
#  set is mutable

# union, difference, intersection


items = set()
elements = {"hello", 123, "python", 10, "Don"}
components = {"car", "truck", "Bike", 123, "python"}

# Can give any iterable in the union, intersection, difference, isdisjoint etc..


# elements.add("Don") # to add an element to a set
# elements.remove(123) # to remove an element from a set
# elements.clear() # clears all elements from the set and returns empty set
# elements.pop() # pops an element from set
print(elements)
print(elements.union(components)) # combines the set and any iterable, can be list, range or any, and returns as a new set
print(elements)
print(elements.difference(components)) # returns the difference of first set from second that is 
# common ones removed from the first set (can also give iterable as the second argument)
print(elements.intersection(components)) # return the common elements between the two sets
print(elements.isdisjoint(components)) # returns true if the two sets are disjoint that is 
# they are completely different(no intersection)
elements.update(components) # updates the first set with the element of the second but returns none
print(elements)

nums = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 5, 8, 9]
nums = list(set(nums))
print(nums)