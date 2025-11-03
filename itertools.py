 # https://docs.python.org/2/library/itertools.html

# # Permutations using itertools
# import itertools

# chars = ['a', 'b', 'c']
# perms = itertools.permutations(chars)

# for p in perms:
#     print(p)

# Combinations using itertools
import itertools
chars = ['a', 'b', 'c']
combs = itertools.combinations(chars, 2)
for c in combs:
    print(c)


