# Set
# ======
# can be defined set()
# Duplicates are not allowed
# order is not preserved
# there are no indexing 
# Iterable but still no indexing and order preserving
#  set is mutable
elements = [12, "hello", "python", "hello", True]
elements = set(elements)
print(elements)

elements.remove(12)
elements.add("Don")
print(elements)