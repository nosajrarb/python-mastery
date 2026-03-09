import numpy as np

test = np.array([1,2,3])
print(type(test))
print("total dimensions ",test.ndim)
print("shape ", test.shape)
print("size ", test.size)
print("data ", test.itemsize)

null = np.zeros((3,3), dtype= np.int32)
print(null)

ones_float = np.ones((1,3), dtype= np.float16)
print(ones_float)

random = np.empty((2,3), dtype= np.float16)
print(random)

evens = np.arange(0, 31, 2)
print(evens)