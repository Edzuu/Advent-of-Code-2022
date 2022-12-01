import numpy as np

arr = []
sum = 0

#Part 1
with open("input.txt") as file:
    for line in file:
        if line.strip():
            sum += int(line)
        else:
            arr.append(sum)
            sum = 0

arr = np.array(arr)
arr_max = np.max(arr)
print(arr_max)

#Part 2
top3 = 0
ind = np.argsort(arr)[::-1][:3]
for i in ind:
    top3 += arr[i]
print(top3)