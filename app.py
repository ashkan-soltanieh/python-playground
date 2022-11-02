from itertools import permutations

input = "011"

output = sum([list(map(list, permutations(input, i))) for i in range(len(input) + 1)], [])

print(output)hi
