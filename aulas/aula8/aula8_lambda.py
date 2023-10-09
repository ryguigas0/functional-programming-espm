def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for i in lista:
        print(i, '==>', funcao(i))

processar('dobros de 1 a 10', range(1,11), lambda x: x * 2)