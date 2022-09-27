import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
#axis=1, NumPy will return the product for each array.#
print(np.prod([arr1, arr2], axis=1))
