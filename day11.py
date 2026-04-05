# numpy basics syntax in python
import numpy as np
normal_list =[1,2,3,4,5]
print(normal_list)
# numpy array creation
numpy_array = np.array(normal_list)
print(numpy_array)
# numpy array operations
numpy_array = numpy_array + 100
print(numpy_array)
# array Creation
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c =np.ones(5)
d = np.arange(0, 10)
print(a,b,c,d)
# shape and reshape
import numpy as np
arr = np.array([1,2,3,4,5,6])

print(arr.shape)      # (6,)
new_arr = arr.reshape(2,3)
print(new_arr)