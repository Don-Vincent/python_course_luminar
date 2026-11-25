students = [
    ["Arun", 21, "kollam"],
    ["Rahul", 23, "Kochi"],
    ["Ram", 25, "Tvm"],
    ["Anu", 24, "Kochi"]
]

# Update the age of anu to 26
students[3][1] = 26
print(students)


# remove details of ram from student
for i in students:
    if "Ram" in i:
        students.remove(i)
print(students)