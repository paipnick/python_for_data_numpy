import numpy as np

arr = np.array([90, 180, 360])

arr = np.around(np.deg2rad(arr),3)
print(arr)

arr = np.around(np.rad2deg(arr),3)
print(arr)
#By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees as well as degress to radians as well.#