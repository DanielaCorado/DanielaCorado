# Exercício de fundamentos de Python : Estrutura de repetição e Condições

# Programa usado para ler o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a) A média de idade do grupo
# b) Qual é o nome do homem mais velho
# c) Quantas mulheres têm menos de 20 anos.

idadegrupo = []
idademulheres = []
idadehomens = []
idadehomemmaisvelho = 0
homemaisvelho = ''

def msg (texto):
    print('--'*20)
    print(texto.center(40))
    print('--'*20)

for c in range (1,5):
    msg(f'{format(c)}°PESSOA')
    nome = str(input('NOME:')).strip().title()
    idade = int(input('IDADE:'))
    sexo  = str(input('SEXO [M/F]:')).strip().upper()
    idadegrupo += [idade]
    if sexo == 'F':
        if idade < 20:
            idademulheres += [idade]
    if sexo == 'M':
        idadehomens += [idade]
        if idade > idadehomemmaisvelho:
            idadehomemmaisvelho = idade
            homemaisvelho = nome

print('--'*20)
print(f'A média das idades do grupo é {sum(idadegrupo)/len(idadegrupo)} anos.')

if len(idadehomens) == 0:
    pass
elif len(idadehomens) == 1:
    print(f'Tem somente um homem no grupo, o {homemaisvelho}.')
else:
    print(f'O homem mais velho tem {max(idadehomens)} anos e é o {homemaisvelho}.')


if len(idademulheres) == 0:
    pass
elif len(idademulheres) == 1:
    print('Somente uma mulher tem menos de 20 anos')
else:
    print(f'No total tem-se {len(idademulheres)} mulheres com menos de 20 anos.')
print('--'*20)
