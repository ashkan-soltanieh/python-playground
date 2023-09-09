import operator

from toolz.curried import get_in, groupby, itemmap, reduce, reduceby

projects = [{'name':'build roads','state':'CA','cost':100},
            {'name':'fight crime','state':'IL','cost':10},
            {'name':'help farmers','state':'IL','cost':200},
            {'name':'help farmers','state':'CA','cost':20}]

print(reduceby('state', lambda acc, x: acc + x['cost'], projects, init=0))
print(get_in([0, "name"], projects)) # output: build roads

def iseven(x):
    return x % 2 == 0

def list_append(list_obj, i):
    list_obj.append(i)
    return list_obj

print(reduceby(iseven, list_append, [1, 2, 3, 4, 1, 2, 3], list)) # -> {False: [1, 3, 1, 3], True: [2, 4, 2]}
print(groupby(iseven, [1, 2, 3, 4, 1, 2, 3]))

account = {"name": "John", "job": "student"}

def capitalize(item):
    k, v = item
    return(k.upper(), v.upper())

print(itemmap(capitalize, account)) # -> {'NAME': 'JOHN', 'JOB': 'STUDENT'}
print({k.upper(): v.upper() for k, v in account.items()}) # -> {'NAME': 'JOHN', 'JOB': 'STUDENT'}

print(reduce(operator.add, [1, 2, 3, 4, 1, 2, 3]))
print(list(map(str, [1, 2, 3, 4, 1, 2, 3])))