# Imperativo
# def fatorial(x):
#     r = 1
#     for i in range(1, x+1):
#         r = r * i
#     return r

# Recursivo normal
def fatorial(x):
    # if x > 0:
    #     return x * fatorial(x - 1)
    # else:
    #     return 1
    return x * fatorial(x -1) if (x -1) > 0 else 1


print(fatorial(5))
