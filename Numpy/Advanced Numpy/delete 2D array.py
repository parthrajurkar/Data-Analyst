import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)

# we want to delete 1st row i.e [1,2,3] from array

#axis = 0 deletes row at given index
arr1_2d=np.delete(arr_2d,0,axis=0)
print(arr1_2d)

#axis = 1 deletes columns at given index
arr2_2d=np.delete(arr_2d,0,axis=1)
print(arr2_2d)

#axis = None(default), flatten array and then deletes element at given index
arr3_2d=np.delete(arr_2d,0,axis=None)
print(arr3_2d)