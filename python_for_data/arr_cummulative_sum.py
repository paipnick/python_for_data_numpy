import numpy as np

arr = np.array([1, 2, 3])
#partially adding the elements in array.E.g. The partial sum of [1, 2, 3] would be [1, 1+2, 1+2+3] = [1, 3, 6]#
print(np.cumsum(arr))
