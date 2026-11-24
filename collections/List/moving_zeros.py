nums = [0, 1, 2, 0, 3, 4, 0, 6, 7, 0] # result = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
# for i in nums:
#     if i == 0:
#         nums.pop(nums.index(i))
#         nums.append(i)
#         # nums.append(nums.pop(nums.index(0)))
# print(nums)


for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)
print(nums)
