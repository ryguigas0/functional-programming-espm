from functools import reduce

nums = range(1,21)

dobros = map(lambda i: i * 2, nums)
pares = filter(lambda i: i % 2 == 0, nums)
somatoria = reduce(lambda i, soma: i + soma, nums, 0)

print(list(dobros))
print(list(pares))
print(int(somatoria))