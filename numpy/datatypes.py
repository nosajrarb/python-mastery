import numpy as np

z = np.arange(3, dtype = np.uint8)
print(z)

# array types can also be reffered using the character codes
w = np.zeros(7, dtype='f')
print(w)

#to determin data type of an array
print(w.dtype)


#convert datatypes
wintergers = w.astype(np.int32)
print(w)
print(wintergers)