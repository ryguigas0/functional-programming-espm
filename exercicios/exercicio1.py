# 1
print('#### Exercício 1')
str = "entrada" 
print(f'{str} invertido é {str[::-1]}')

# 2
print('#### Exercício 2')
frase = "Python é uma linguagem excelente"

tem_py = 'py' in frase
tem_ing = 'ing' in frase
tem_zz = 'zz' in frase

print(f'Contém "py"? {tem_py}')
print(f'Contém "ing"? {tem_ing}')
print(f'Contém "zz"? {tem_zz}')

# 3
print('#### Exercício 3')
salario = 3450.45
despesas = 2456.2

percent = despesas / salario

print('Percentual do salário (R${:.2f}) comprometido pelas despesas ({:.2f}) é: {:.2f}'.format(salario, despesas, percent))

# 4
# print('#### Exercício 4')
# x = float(input("Digite um número: "))
# y = float(input("Digite um número: "))

# print(f'{x} + {y} = {x+y}')

# 5
print('#### Exercício 5')
palavra = 'paralelepípedo'
output = ''

for c in list(palavra):
    output += f'{c},'

print(output)

# 6
print('#### Exercício 6')
nomes = ['Danieli', 'André', 'Marcelo', 'Ana Paula']
for n in nomes:
    print(n)

# 7
# print('#### Exercício 7')
# from random import randint

# n = randint(0, 9)

# chute = int(input("Digite um número de 0 a 9: "))

# if chute == n:
#     print(f"Número secreto {n} foi encontrado!")

# 8
print('#### Exercício 8')
ini = int(input("Digite o indíce de início de sequência de saída: "))
limit = (ini + 10)

fib_list = [0, 1]
for n in range(1, limit - 1):
    fib_list.append(fib_list[n - 1] + fib_list[n])

print(f'A sua sequência de 10 números depois de {fib_list[ini-1]}: {fib_list[ini:]}')


