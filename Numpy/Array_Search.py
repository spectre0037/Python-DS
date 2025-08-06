# To search an array, use the where() method.
import numpy as np
array = np.array([1,2,3,4,5,6])
# x = np.where(array==5)
# y = np.where(array%2 == 0)
# z = np.where(array%2 == 1)
# print(x) #Finds the index where the value is 5
# print(y) #Finds the index where the values are even
# print(z) #Finds the index where the values are odd


#Using seacrhsorted() method
#The searchsorted() method is assumed to be used on sorted arrays.

# a = np.searchsorted(array,6) # Finds the index where the value 6 is supposed to be
# print(a)
# You can also use the search sorted method for array value that is supposed to come after the last index for example in this case 7

# b = np.searchsorted(array,5,side='right') # Finds the index where value 7 is supposed to come from right
# print(b)

#Multi value search
array_2 = np.array([1,3,5,7])
c = np.searchsorted(array_2,[2,4,6])
print(c)