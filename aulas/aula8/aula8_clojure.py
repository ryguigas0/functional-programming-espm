def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

dobro = multiplicar(2)
triplo = multiplicar(3)
meio = multiplicar(0.5)

print(dobro(5))
print(triplo(6))
print(meio(7))