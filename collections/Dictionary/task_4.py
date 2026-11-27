scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
# keep only scores > 60

for key, val in scores.copy().items():
    if val <= 60:
        scores.pop(key)
print(scores)

for i in scores.copy():
    if scores[i] <= 60:
        scores.pop(i)
print(scores)