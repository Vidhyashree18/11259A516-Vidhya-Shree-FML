import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)

import numpy as np

a = np.array([10, 20, 30, 40])

print("Sum:", np.sum(a))

import numpy as np

a = np.array([12, 45, 23, 67, 9])

print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print(b)

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)

import numpy as np

a = np.array([2, 4, 6])
b = np.array([3, 5, 7])

print("Multiplication:", a * b)

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Transpose:")
print(a.T)


import numpy as np

a = np.array([[1, 2],
              [3, 4]])

print("Determinant:", np.linalg.det(a))
