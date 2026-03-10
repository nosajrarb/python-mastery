import numpy as np

x = np.arange(1,5) #start from 1 and end  before 5
print(x)
print("first element: ", x[0])
print("last elemetnt: ", x[-1])
print("second last elemnet: ", x[-2])

y = np.arange(9).reshape((3,3))
print(y)

z = y.reshape(9)
print(z)