import numpy as np

# array = np.array([1,2,3,4,5])
x = [True,False,True,False,True]
new_array = array[x] # This will filter the array by removing the values on the index where there is false on x

print(new_array)


# Create a filter array that will return only values higher than 42

array = np.array([41,42,43,44])

filter_list = [] # Creating a filter list

for element in array:
    if element >42:
        filter_list.append(True)
    else:
        filter_list.append(False)

filtered_array = array[filter_list]

print("FILTER LIST",filter_list)
print("FILTERED ARRAY :",filtered_array)


#Create a filter that will only return the even value from an array

array = np.array([41,42,43,44])

filter_list = [] # Creating a filter list

for element in array:
    if element%2 == 0:
        filter_list.append(True)
    else:
        filter_list.append(False)

filtered_array = array[filter_list]

print("FILTER LIST",filter_list)
print("FILTERED ARRAY :",filtered_array)

#ALternate method

array = np.array([41,42,43,44])

filter_list = array >42

filtered_array = array[filter_list]

print("FILTER LIST",filter_list)
print("FILTERED ARRAY :",filtered_array)