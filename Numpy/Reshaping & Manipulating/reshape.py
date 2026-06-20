"""
Reshape changes the shape of Array,But Elements remain the same,
Syntax - reshape(rows,columns)
this fn works only if Dimension is same before and after
"""

import numpy as np
arr =np.array([1,2,3,4,5,6])
print(arr)

reshape_arr=arr.reshape(2,3)
print(reshape_arr)