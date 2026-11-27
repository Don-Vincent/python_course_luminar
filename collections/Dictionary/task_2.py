keys = ["name", "age", "place"]
values = ["sukumar", "27", "kochi"]
student = {}
for i in range(len(keys)):
    student[keys[i]] = values[i]
print(student)

stud = {}
for i, j in zip(keys, values):
    stud[i] = j
print(stud)
