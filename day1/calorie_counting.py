import numpy as np

arr = []
sum = 0
with open("input.txt") as file:
    for line in file:
        if line.strip():
            sum += int(line)
        else:
            arr.append(sum)
            sum = 0

arr = np.array(arr)
arr = np.max(arr)
print(arr)