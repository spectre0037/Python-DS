import numpy as np

array_1 = np.array([1,2,3,4,5])
copy_array = array_1.copy()
array_1[0] = 2

print("\nVALUE OF ARRAY 1",array_1)
print ('\nVALUE OF COPY OF ARRAY 1',copy_array)


view_array = array_1.view()
array_1[0] = 2
print("\nVALUE OF ARRAY 1",array_1)
print("\nVALUE OF VIEW ARRAY ",view_array)


# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

# Print the value of the base attribute to check if an array owns it's data or not:
x = array_1.copy()
y = array_1.view()

print("\nBASE VALUE OF ARRAY X",x.base)
print("\nBASE VALUE OF ARRAY Y",y.base)