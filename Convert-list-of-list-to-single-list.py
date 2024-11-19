import itertools

geek = [[1, 2], [3, 4], [5, 6]]


lst = list(itertools.chain.from_iterable(geek))
print(lst)