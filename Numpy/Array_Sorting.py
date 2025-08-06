import numpy as np

#Sorting a 1D array
array   = np.array([1,2,3,5,3,4,9,7])
sorted_array = np.sort(array)
print(sorted_array)

#Sorting a string array
array_2 = np.array(['banana', 'cherry', 'apple'])
sorted_array_2 = np.sort(array_2)
print(sorted_array_2)

#Sorting a Boolean array
array_3 = np.array([True, False, True])
sorted_array_3  = np.sort(array_3)
print(sorted_array_3)

#Sorting a 2D array
array_4   = np.array([[3, 2, 4], [5, 0, 1]])
sorted_array_4 = np.sort(array_4)
print(sorted_array_4)