# HOF == High Order Functions

from aulas.aula8.aula8_prim_class import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for i in lista:
        print(i, '==>', funcao(i))

processar('Dobros de 1 a 10', range(1,11), dobro) # HOFs acontecem quando uma função recebe outra função
processar('Quadrados de 1 a 10', range(1,11), quadrado)