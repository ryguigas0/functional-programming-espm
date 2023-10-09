def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

a = dobro(10)
b = dobro(10)
c = dobro # guarda uma referência a função dobro
d = c(20) # pdoe ser chamado para rodar