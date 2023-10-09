from functools import reduce

def progredir(n, a1, r):
    return a1 + (n - 1) * r

def progressao_arit(ini, fim):
    return list(map(lambda x: progredir(x+1, range(ini, fim+1)[0], 1), range(ini, fim+1)))

def somatoria(lista):
    return reduce(lambda s,x: s + x, lista, 0)

print(int(somatoria(progressao_arit(0, 5))))