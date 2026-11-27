"""
Dictionary
==========

dict = {"Name":"Don", "Age": 23, "Weight": 56}
elements in dictionary are key value pairs


can be defined using dict = {} or dict()

cannot give same key for two values. if we give same key the dictionary will only take the latest one, that means the last one

key whould be an integer or a string

• The dict() Constructor. Creates a dictionary using keyword arguments (dict(name="Alice", age=25)) or 
by passing a list of key-value tuples (dict([("name", "Alice"), ("age", 25)])).

Dictionary Comprehension. Dynamically builds a dictionary from an iterable in a single line 
dict = {x: x**2 for x in range(3)}.

Direct Key Iteration. Looping directly over a dictionary (for key in d:) 
traverses its keys in insertion order without needing extra method calls. 
You can also explicitly use for key in d.keys():.

Value Iteration with .values(). Looping over d.values() (for val in d.values():) 
yields each value directly when you do not need the keys.

Key-Value Pair Iteration with .items(). Using for key, val in d.items(): 
returns each pair as a tuple and unpacks them into separate variables for clean access to both.

"""

dict = {"name":"Don", "age": 23, "weight": 56, "place": "Thodupuzha"}

dict_2 = {x: x ** 2 for x in range(1, 6)}
print(dict_2)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(dict["name"])

for key in dict:
    print(dict[key])

print("\n")

for key in dict.keys():
    print(dict[key])

print("\n")
dict["place"] = "Delhi"

for val in dict.values():
    print(val)

print("\n")
for key, val in dict.items():
    print(f"{key} : {val}")


from collections import Counter
dict_3 = [1, 2, 3, 1, 1, 5, 5, 7, 2, 2]
counts = Counter(dict_3)
print(counts)
print(counts.most_common(1))


# Methods


print(dict.get("name","Vincent" )) #Return the value for key if key is in the dictionary, else default here default is "Vincent"

print(dict.keys()) # dict_keys(['name', 'age', 'weight', 'place'])
print(dict.values()) #dict_values(['Don', 23, 56, 'Delhi'])
print(dict.items()) #dict_items([('name', 'Don'), ('age', 23), ('weight', 56), ('place', 'Delhi')])
print(dict.pop("name")) # Don
