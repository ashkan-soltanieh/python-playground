from functools import partial, reduce
import numpy as np
from operator import add
from toolz.functoolz import curry, compose_left
from itertools import permutations, product

config = "1, 0, 1, 1, 0, 0"
convert_delimeted_config_to_array = partial(np.fromstring, dtype=int, sep=",")
myarray = convert_delimeted_config_to_array(config)
print(myarray)  # -> array([1 0 1 1 0 0])

convert_config_to_array = curry(np.fromstring, dtype=int, sep=",")
myarray = convert_config_to_array(config)
print(myarray)  # -> array([1 0 1 1 0 0])

########################
# Reduce(binaryFunc, iterable)

myarray = np.array([1, 1, 1])
sum_result = reduce(add, myarray)
print(sum_result)

######################

config_count = 3
availability_base = "1" + "0" * (config_count - 1)
convert_iterables_to_array_as_int = curry(np.fromiter, dtype=int)
convert_nested_iterables_to_array_as_int = curry(np.fromiter, dtype= np.dtype((int, config_count)))
get_all_possible_availabilities_for_specified_configs = curry(permutations, r=config_count)

possible_availabilities = compose_left(convert_iterables_to_array_as_int, 
                                       get_all_possible_availabilities_for_specified_configs,
                                       set,
                                       convert_nested_iterables_to_array_as_int)(availability_base)

configs = compose_left(curry(product, repeat=config_count), 
                       curry(np.fromiter, dtype= np.dtype((int, config_count))))([1, 0])

joined_configs = product(configs, possible_availabilities)

filter_joined_configs = lambda joined_config: any(np.flatnonzero(joined_config[0]) == np.flatnonzero(joined_config[1]))

filtered_joined_configs = list(filter(filter_joined_configs, joined_configs))

convert_array_items_to_str = curry(map, str)

def make_string_from_list(list_obj):
    return "".join(list_obj)

joined_configs_as_string = compose_left(np.concatenate, convert_array_items_to_str, list, make_string_from_list)

print(list(map(joined_configs_as_string, filtered_joined_configs)))

