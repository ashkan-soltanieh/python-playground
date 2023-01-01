from itertools import permutations
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

# Creating NumPy Arrays from honogenous non-list iterables - 2D
# -> {(1, 0, 0), (0, 0, 1), (0, 1, 0)}
configs = set(permutations([0, 0, 1], 3))
myarr = np.fromiter(configs, dtype=np.dtype((int, 3)))
print(myarr.shape)  # -> (3, 3)

# Creating NumPy Array from string literals no delimiter with type conversion - 1D
mystr = '101'
myarr = np.fromiter(mystr, dtype=int)
print(myarr)  # -> array([1 0 1])

# Creating NumPy Array from string literals with delimiter with type conversion - 1D
mystr = "1, 0, 1, 0"
myarr = np.fromstring(mystr, dtype=int, sep=",")  # -> array([1, 0, 1, 0])
print(myarr)

# Creating NumPy Array with type conversion - 1D
mylist = ["1", "2", "3"]
myarr = np.fromiter(mylist, dtype=int)
print(type(myarr[0]))  # -> <class 'numpy.int64'>

# Creating NumPy Array with type conversion - 2D
mylist = [['1', '0'], ['1', '0'], ['1', '1']]
myarr = np.fromiter(mylist, dtype=np.dtype((int, 2)))
print(myarr.shape)  # -> (3, 2)
print(type(myarr[0][0]))  # -> <class 'numpy.int64'>

# Creating NumPy Array with type conversion - nD
mylist = [[['1', '3', '5'], ['0', '3', '5']],
          [['1', '3', '5'], ['0', '3', '5']]]  # -> shape: 2*2*3
myarr = np.fromiter(mylist, dtype=np.dtype((int, (2, 3))))
print(myarr.shape)  # -> (2, 2, 3)
print(type(myarr[0][0][0]))  # -> <class 'numpy.int64'>

###############################

# Convert array to list of same datatype - nD
myarr = np.array([1, 2, 3])
mylist = myarr.tolist()  # -> whole array including the nested arrays converted to list

###############################

# Convert numbers array to joined strings - 1D
myarr = np.array([1, 2, 3])
mystr = "".join(map(str, myarr))
print(mystr)  # -> "123"

mystr = "".join(np.char.mod("%s", myarr))
print(mystr)  # -> "123"

# Convert numbers array to joined strings - 2D
myarr = np.array([[1, 2], [3, 4]])
mystr = ["".join(map(str, row)) for row in myarr]
print(mystr)  # -> ["12", "34"]

mystr = ["".join(row) for row in np.char.mod("%s", myarr)]
print(mystr)  # -> ["12", "34"]

###############################
