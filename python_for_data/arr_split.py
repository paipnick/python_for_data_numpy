import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

arrList = np.array_split(arr, 3)

for arr in arrList:
    print(arr)
