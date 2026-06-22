#this check any infinite value  in array
#syntax- numpy.isinf(array)

import numpy as np

arr=np.array([10,20,np.inf,30,40,-np.inf])
#return true wherever +,- infinite value is found
print(np.isinf(arr))
