marks = {"arun":{"python":85,"sql":67,"ai":65},
         "rahul":{"python":91,"sql":73,"ai":70},
         "amal":{"python":80,"sql":60,"ai":79}
         }
# return the sum of marks of each student


result = {}
for i in marks:
    result[i] = sum(marks[i].values())
print(result)



# return the average of mark of each students


avg = {}
for i in marks:
    avg[i] = sum(marks[i].values()) / len(marks[i])
    # avg[i] = round(sum(marks[i].values()) / len(marks[i]), 2)
print(avg)


# return the name of students scored above 65 in sql

res = []
for i in marks:
    if "sql" in marks[i] and marks[i]["sql"] > 65:
        res.append(i)
print(res)

print([i for i in marks if "sql" in marks[i] and marks[i]["sql"] > 65])



# task

# list where each key is sub and value is the average of mark of each student of that sub
