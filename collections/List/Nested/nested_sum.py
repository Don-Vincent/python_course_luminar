items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = []

# for i in range(3):
#     result.append(items[0][i] + items[1][i] + items[2][i])
# print(result)

result = []
for i in range(len(items[0])):
    total = 0
    for j in items:
        total += j[i]
    result.append(total)
print(result)


# result = [0, 0, 0]
# for i in items:
#     result[0] += i[0]
#     result[1] += i[1]
#     result[2] += i[2]
# print(result)




    
