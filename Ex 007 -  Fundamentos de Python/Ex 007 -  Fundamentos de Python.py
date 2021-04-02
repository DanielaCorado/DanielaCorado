# Exercício de fundamentos de Python : Bibliotecas Pandas

# Exercício para praticar habilidades com Pandas, analisando o DataFrame Ecommerce Purchases

import pandas as pd

def enunciado(msg):
    print('--' * 40)
    print(msg.center(80))
    print('--' * 40)
    return

enunciado('DataFrame:')
econ = pd.read_csv('Ecommerce Purchases')
print(econ.head())

enunciado('Informações Sobre o DataFrame:')
print(econ.info())

enunciado('Preço de compra médio:')
print(econ['Purchase Price'].mean())

enunciado('Preço Máximo e Mínimo:')
print(f"Preço de compra máximo é {econ['Purchase Price'].max()}")
print(f"Preço de compra mínimo é {econ['Purchase Price'].min()}")

enunciado('Número de pessoas com Inglês:')
def ingles (title):
    if 'en' in title:
        return True
    else:
        return False
print(sum(econ['Language'].apply(lambda x:ingles(x))))

enunciado('Número de pessoas com cargo de advogado:')
print(econ[econ['Job'] == 'Lawyer'].shape)

enunciado('Número de pessoas que fizeram compras de manhã e a tarde:')
print(econ['AM or PM'].value_counts())

enunciado('As cinco profissões mais comum:')
print(econ['Job'].value_counts().head())

enunciado('Preço da compra feito no lote 90 WT :')
print(econ[econ['Lot'] == '90 WT'] ['Purchase Price'])

enunciado('Email da pessoa com cartão XXX :')
print(econ[econ['Credit Card'] == 4926535242672853] ['Email'])

enunciado('Quantas pessoas tem American Express como cartão:')
print(sum(econ[econ['CC Provider'] == 'American Express'].value_counts()))

enunciado('Quantas pessoas com American Express fex compras acima de 95US')
print(sum(econ[econ['CC Provider'] == 'American Express'].value_counts() & (econ[econ['Purchase Price'] >= 95].value_counts())))

enunciado('Pessoas com cartão que expiram em 2025')
print(sum(econ['CC Exp Date'].apply(lambda x: x[3:]) == '25')) # Pega só o final

enunciado('Provedor de e-mail mais comum')
print(econ['Email'].apply(lambda x: x.split('@')[1]).value_counts().head())
