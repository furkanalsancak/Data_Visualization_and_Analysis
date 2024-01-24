import numpy as np

lista = [2,4,5,6,8]

# array function
print("array function")
numpy_array = np.array(lista)
print(numpy_array)

print()

# zeros function
print("Zeros function")
print(np.zeros(10))
print(np.zeros((3,4)))

print()

# arange
print("arange function")
print(np.arange(5))
print(np.arange(1,10,2))

print()

# rand
print("rand function")
print(np.random.rand(10) * 10) # scalar multiplication

print()

# N dimensions
print("N dimensions")
print(np.array([[1,2,3],[4,5,6]]))

print()

# full function
print("Full function")
print(np.full((2,2), (5,3)))
print(np.full((6,3), (10,24,32)))

print()

# rand 2d
print("rand 2d")
print(np.random.rand(3,5) * 100)
print(np.random.rand(3,5,4) * 100)

print()

# empty
print("empty")
print(np.empty((2,2)))

print()

# Data types
# int64 is default data type in numpy
print("Data types")
num_array = np.array([1,2,3,4,5], dtype='int64')
print(num_array.astype('float'))
# print(np.empty((2,2)).ndim)
print(np.array([1+2j, 2+2j]).dtype)