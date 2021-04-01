# Exercício de fundamentos de Python : Estrutura de repetição, Condições e Listas

# Faça um programa que leia o nome e o peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = list()
prin = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome:')).strip().title())
    temp.append(float(input('Peso:')))
    if len(prin) == 0:
        maior = menor = temp [1]
    else:
        if temp[1] > maior:
            maior =  temp [1]
        if temp[1] < menor:
            menor = temp [1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar:[S/N]')).strip().upper()[0]
    if resp != 'S' and resp!= 'N':
        print('Opção Inválida!')
        resp = str(input('Deseja continuar:[S/N]')).strip().upper()[0]
    elif resp == 'N':
        break

print('-='*20)
print(f'Ao todo você cadastrou {len(prin)} pessoas.')
print(f'O maior peso cadastrado foi de {maior} Kg, peso de',end=' ')
for p in prin:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')

print()
print(f'O menor peso foi de {menor} Kg, peso de',end=' ')
for p in prin:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')

print('-='*20)

