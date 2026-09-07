# Find the largest number in a list.


num = [6,3,5,2]
print(max(num))
largeNum = num[0]
# print(largeNum)
for items in num:
    if items > largeNum:
        largeNum = items
print(largeNum)