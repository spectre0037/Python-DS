import numpy as np
# Iterating through a 1-D array
arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)
#Iterating through a 2-D array
arr_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for y in arr_2:
    for z in y:
        print(z)
#Iterating through a 3-D array
arr_3 = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

for a in arr_3:
    for b in a:
        for c in b:
            print(c)