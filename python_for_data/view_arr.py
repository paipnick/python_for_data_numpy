import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view = arr.view()

view[0] = 24
view[2] = 40
print(arr)
print(view)
