# Exercício de fundamentos de Python : Função

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular
# Outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial (n, show = False):
    """
    -> Cálcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostar ou não os cálculos
    :return: O valor fatorial de um númeor n.
    """
    f = 1
    for c in range (n,0,-1):
        if show :
            print(c,end='')
            if c > 1:
                print(f' x ', end= '')
            else:
                print(' = ', end='')
        f *= c
    return f

def msg (texto):
    print('--'*20)
    print(texto.center(40))
    print('--'*20)

# Programa Principal
msg('Fatorial de 5 com os cálculos :')
print(fatorial(5, True))
msg('Fatorial de 4 :')
print(fatorial(4))
msg('Help da função fatorial : ')
help(fatorial)
