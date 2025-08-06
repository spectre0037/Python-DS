# SHAPE OF AN ARRAY IS THE NUMBER OF ELEMENT IN EACH DIMENSION
import numpy as np

array = np.array([1,2,3,4,5])
array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
array_2 = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
print(array.shape)
print(array_1.shape)
print(array_2.shape)