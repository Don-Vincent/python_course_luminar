# Tuple 
# ========

# it can be defined using () or tuple()
# order is preserved
# indexed(0 based)
# Duplicates are allowed
# hetrogenous
# Tuple is immutable
# example

items = ("python", 10, True, "python")
# or
# items = tuple("python", 10, True, "python")

items.index("python")
# returns index of first occurance of a value

items.count("python")
# return the count of occurance of a value

new = list(items)
new = new.append("helloworld")
new = tuple(new)
print(new)