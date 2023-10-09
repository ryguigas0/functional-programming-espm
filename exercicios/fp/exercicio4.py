from functools import reduce

def fib(n):
    return list(reduce(lambda fib_list, x: fib_list + [fib_list[x-1] + fib_list[x-2]], range(2, n), [0, 1]))

print(fib(10))