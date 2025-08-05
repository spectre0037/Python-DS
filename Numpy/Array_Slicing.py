import numpy as np

#Slice from 1 index element to the one before 3 index
# array = np.array([1,2,3,4,5])
# print(array[1:3])

#Slice from 1 index to the end
# print(array[1:])

#Slice from start till the index before the index 4
# print (array[:4])

#Slice from the index 3 from the end to the index 1 from the end
# print(array[-3:-1])

#Slice with step : start from index 0 till the index before 5 and pick every 3rd element
# print(array[0:5:3]) # [start:stop:step]

#--------------------------------------------------------------------------------

#Slicing 2-D arrays
two_D_array = np.array([[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]])

print(two_D_array[1,1:9:2]) #printing every 2n element from the second array



