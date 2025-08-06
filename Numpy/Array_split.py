import numpy as np
# #Spliting one dimensional array
# array_1 = np.array([1,2,3,4,5,6])
# newarr = np.array_split(array_1,3)
# print(newarr)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# #Spliting 2 dimensional array
# array_2 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
# newarr_2 = np.array_split(array_2,3)
# print(newarr_2)

# #Spliing 2 dimensional array into another 2 dimensional array
# array_3 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
# newarr_3 = np.array_split(array_3,3,axis=1)
# print(newarr_3)

#ALternate methhod 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)