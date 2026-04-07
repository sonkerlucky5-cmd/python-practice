# numpy Boolean indexing
import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8])
bool_idx = (arr > 4)
print(bool_idx)
print(arr[bool_idx])  
# numpy fancy indexing
import numpy as np 
arr = np.array([10,20,30,40,50])
indices = [0, 2, 4]
print(arr[indices])
# numpy broadcasting
import numpy as np
arr = np.array([1,2,3])
print(arr + 10)
# numpy Aggregations (Math & Stats)
import numpy as np 
salaries = np.array([50000, 60000, 55000, 70000, 65000])
print("Total salaries:", np.sum(salaries))
print("Average salary:", np.mean(salaries))
print("Maximum salary:", np.max(salaries))
print("Minimum salary:", np.min(salaries))
highest_salary = np.argmax(salaries)
print("index of highest salary:", highest_salary)
# NumPy Random Array & Filtering (Boss Level Task)
import numpy as np
random_arr = np.random.randint(1, 100, size=10)
print("Original Random Array:", random_arr)
print("Maximum Value:", np.max(random_arr))
chote_numbers = random_arr[random_arr < 50]
print("Numbers less than 50:", chote_numbers)
# numpy parctice
import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
print("original array:", arr)
print("array after adding 5:", arr + 5)
print("array after multiplying by 2:", arr * 2)
print("array after squaring:", arr ** 2)
print("mean of the array:", np.mean(arr))
print("standard deviation of the array:", np.std(arr))