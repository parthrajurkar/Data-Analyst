# astype is used to convert data type of array elements
#syntax - arr.astype(datatype)

import numpy as np
arr=np.array([1.2,2.6,3.9,4.0])
print(arr)
print(arr.dtype)

arr_1=arr.astype(int)
print(arr_1)
print(arr_1.dtype)