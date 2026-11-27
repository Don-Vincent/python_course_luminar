expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
# output >> Total expenses: 1850

total = 0
for key in expenses:
    total += expenses[key]
print("Total expense:", total)


tot = sum(expenses.values())
print(tot)

t = 0
for val in expenses.values():
    t += val
print(t)

arr = [1, 2, 5]