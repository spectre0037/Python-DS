import numpy as np

# # JOINING TWO 1-D ARRAYS
# array_1 = np.array([1,2,3,4,5])
# array_2 = np.array([6,7,8,9,10])

# arr = np.concatenate((array_1,array_2))
# print(arr)

# array_3 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# array_4 = np.array([[6,7,8,9,10],[6,7,8,9,10]])

# arr_1 = np.concatenate((array_3,array_4),axis=1)
# print(arr_1)


# Using stack to join arrays
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# Stack along rows
arr_2 = np.hstack((arr1,arr2))
print(arr_2)

#stack along column
arr_3 = np.stack((arr1,arr2))
print(arr_3)

#stacking along depth
arr_4 = np.dstack((arr1,arr2))
print(arr_4)