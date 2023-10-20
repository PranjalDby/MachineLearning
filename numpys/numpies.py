import numpy as np
from numpy import ufunc
"""
RULES OF BROADCASTING TWO ARRAYS::
1. if the arrays do not have the same rank,prepend the shape of the lower rank array with 1's until both shapes have the same length

2. 
The two arrays are compatible in adimension if they have the same size in the dimension,or if one of the array has size 1 in that dimension

....
"""

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Note 
# for broadcasting happend we have to ensure that the columns of first matrix is equal to the size of vector we are adding.

# universal function generally used for broadcasting


added_ = np.ones((3,1))

broad = arr + added_

print(broad)

# reshaping 
adds = np.array(np.arange(9),dtype=np.float64).reshape((3,3))
print(adds)

print("some universal functions...")

print(np.add.reduce(adds,axis=(0,1)))

# some more refferences

new_arr = np.c_[np.array([1,2,3]),np.array([4,5,6]),np.array([7,8,9])]
new_2d = np.c_[np.array([[1,2,3]]),0,0,np.array([[4,5,6]])]
print(new_2d)
n_r = np.r_[-1:1:6j,[0] * 3,5,6]
print(n_r)

print("Nicer way to build up index tuples for arrays")

index_exps = np.s_[1::1]
print(index_exps)
# other way is using index_exp which always return a tuple
tuple_index = np.index_exp[2::2]
print(tuple_index)
print(new_arr)
print(np.transpose(np.nonzero(new_arr)))
# numpy.where
a = np.arange(10)
print(np.where(a < 5,a,10 * a))
# it also work for multi-dimensional array
print(np.where([[True,False],
                [True,True]],
                [[1,3],
                 [6,9]],
                 [[11,10],
                  [8,2]]))

x,y = np.ogrid[:3,:4]
print(np.where(x < y,x,10 + y))
