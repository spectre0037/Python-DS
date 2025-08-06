import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(6, 2)

print(arr)
print(newarr)


#FLATENING THE ARRAY
arr_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
newarr_2 = arr_2.reshape(-1)
print(arr_2)
print(newarr_2)
