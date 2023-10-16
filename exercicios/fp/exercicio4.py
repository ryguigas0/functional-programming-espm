fib = lambda n, a=1, b=1: [b,0][n>0] or fib(n-1, b, a+b)

for i in range(0, 8):
    print(fib(i))