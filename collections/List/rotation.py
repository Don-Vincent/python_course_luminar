items = ["hello", 1, 2, "python", "django", 10]

# output>> ["django", 10, "hello", 1, 2, "python"]

for _ in range(2):
    element = items.pop()
    items.insert(0, element)
print(items)