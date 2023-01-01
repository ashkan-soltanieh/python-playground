import numpy as np

# Creating NumPy Array from a list of numbers - 1D
mylist = [1, 2, 3]
myarr = np.array(mylist)

print(myarr)  # -> array([1, 2, 3])

# Creating NumPy Array from a homogeneous list of lists numbers - nD

mylist = [[[1, 0], [2, 4], [5, 1]],
          [[7, 3], [2, 8], [9, 5]]]  # -> 3D array 2*3*2
myarr = np.array(mylist)

print(myarr)  # -> whole array and nested array converted to numpy array
print(myarr.size)  # -> 12
print(myarr.dtype)  # -> int64
print(myarr.shape)  # -> (2, 3, 2)
print(myarr.ndim)  # -> 3

#########################
