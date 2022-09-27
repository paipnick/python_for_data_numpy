import numpy as np

arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4])
#sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.#
print(np.around(np.sin(arr), 3))
print(np.around(np.cos(arr), 3))
print(np.around(np.tan(arr), 3))