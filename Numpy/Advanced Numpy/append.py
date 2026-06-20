#append is used when values need to be inserted at end of the array
# syntax - numpy.append(array,values)

import numpy as np
arr = np.array([10,20,30])
print(arr)
new_arr=np.append(arr,[40,50,60])
print(new_arr)