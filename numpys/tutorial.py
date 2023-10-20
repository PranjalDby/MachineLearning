import numpy as np

# mastering shape

array = np.array([
    29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
   12.6, 49.9, 38.6, 31.3, 9.2, 22.2
]).reshape(2,2,3)
print("after swaping axes in array")
array = array.swapaxes(2,1)
print(array)

# working on axes
table = np.array(
    [
        [5,6,9,8],
        [1,2,3,10]
    ]
)
print(table[0:2,2:4])