# Funções Solicitadas :
def dobro (preco = 0, formatado =False):
    res = preco*2
    return res if formatado is False else moeda(res)

def metade (preco = 0,formatado = False):
    res = preco/2
    return res if formatado is False else moeda(res)

def aumentar (preco= 0,taxa = 0,formatado = False):
    res = preco + (preco * (taxa/100))
    return res if formatado is False else moeda(res)

def diminuir (preco=0, taxa = 0,formatado = False):
    res = preco - (preco * (taxa/100))
    return res if formatado is False else moeda(res)

def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar =5):
    print('--'*15)
    print('RESUMO DO VALOR'.center(30))
    print('--'*15)
    print(f'O preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preco,taxaa,True)}')
    print(f'Com {taxar}% de redução: {diminuir(preco,taxar,True)}')
    print('--'*15)


