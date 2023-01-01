from functools import partial, reduce
import numpy as np
from operator import add

config = "1, 0, 1, 1, 0, 0"
convert_config_to_array = partial(np.fromstring, dtype=int, sep=",")
myarray = convert_config_to_array(config)
print(myarray)  # -> array([1 0 1 1 0 0])

########################
# Reduce(binaryFunc, iterable)

myarray = np.array([1, 1, 1])
sum_result = reduce(add, myarray)
print(sum_result)
