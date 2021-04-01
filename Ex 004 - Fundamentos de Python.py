# Exercício de fundamentos de Python : Função e Dicionário

# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# A) Quantidade de notas
# B) Maior nota
# C) Menor nota
# D) Média da turma
# E) Situação (opcional)

def notas (*n, sit = False ):
    """
    -> Análise das notas dos alunos
    :param n: Notas do aluno
    :param sit: Situação do aluno (opcional)
    :return: Retorna o total de notas, a maior, a menor, a média e a situação
    """

    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = (sum(n)/len(n))
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Ótima'
        if 5 <= r['Média'] < 7:
            r['Situação'] = 'Moderada'
        if r['Média'] < 5:
            r['Situação'] = 'Péssima'
    return r

def msg (texto):
    print('--'*20)
    print(texto.center(40))
    print('--'*20)

# Programa Principal
msg('Exemplo 1:')
ex1 = notas ( 4,5,6,8,sit = True)
print (ex1)

msg('Exemplo 2:')
ex2 =notas(5,8,7,2,9)
print(ex2)

msg('Help da funão notas:')
help(notas)




