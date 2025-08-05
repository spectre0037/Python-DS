import numpy as np

# ## CREATING ARRAYS IN NUMPY
# array = np.array([1,2,3])
# print("Array:", array)
# print ("Type of array:", type(array))

# ## Using tuple to create an array
# array_from_tuple = np.array((4, 5, 6))
# print ("Array form tuple ",array_from_tuple)
# print ("Type of array",type(array_from_tuple))

# # Creating a 0-D array
# OD_array = np.array(42)
# print(OD_array)

# #one dimensional array
# one_D_array = np.array([1,2,3])
# print("One dimensional array",one_D_array)

# # Two dimensional array
# two_D_array = np.array([[1,2,3],[4,5,6]])
# print("Two dimensional array",two_D_array)

# Three dimensional array
# three_D_array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print ("Three dimensional array",three_D_array)

#check the dimensions of the array
# OD_array = np.array(42)
# one_D_array = np.array([1,2,3])
# two_D_array = np.array([[1,2,3],[4,5,6]])
# three_D_array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(OD_array.ndim)
# print(one_D_array.ndim)
# print(two_D_array.ndim)
# print(three_D_array.ndim)

#Higher dimensional arrays
#Creating a 5 dimensional array
#The previous method id inefficient and long so we use alternate method 
# five_D_array = np.array([1,2,3,4],ndmin=5)  # notice here the keyword is ndmin and not ndim
# print (five_D_array)
# print(five_D_array.ndim)



