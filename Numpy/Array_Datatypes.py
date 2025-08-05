import numpy as np

array = np.array([1.1,2.1,3.1])
#How to figure out what the data type of the array is 
print(array.dtype)
#changing the data type of array to int
new_array = array.astype(int)
print(new_array.dtype)
#Changing the datatype of array to bool
new_array_2 = array.astype(bool)
print(new_array_2.dtype)