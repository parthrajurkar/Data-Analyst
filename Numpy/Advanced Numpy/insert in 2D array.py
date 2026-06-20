import numpy as np

arr=np.array([[1,2],[3,4]])

# insert a new row at index 1,axis=0,adds new row betwn [1 2] and [3 4]
# horizontally(row)
new_arr=np.insert(arr,1,[5,6],axis=0)
print(new_arr)

#axis=1 adds new columns betwn [1 2] and [3 4],vertically (column)
new_arr1=np.insert(arr,1,[5,6],axis=1)
print(new_arr1)

#if axis not given or  axis=None,then array is flatten(),Multi-D Array
#is converted to 1D array
#arr becomes [1 2 3 4],then at index 1 [5,6] is inserted
#O/P- [1 5 6 2 3 4]

new_arr2=np.insert(arr,1,[5,6],axis=None)
print(new_arr2)



