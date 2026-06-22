# nan_to_num replaces num value with given number
#syntax - numpy.nan_to_num(array,nan=value) default - 0

import numpy as np
arr=np.array([10,20,np.nan,40,50,np.nan])
print(np.isnan(arr))

new_arr=np.nan_to_num(arr,nan=100)
print(new_arr)