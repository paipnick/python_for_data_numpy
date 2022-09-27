import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()

copy[0] = 24
copy[3] = 30

print(arr)
print(copy)
