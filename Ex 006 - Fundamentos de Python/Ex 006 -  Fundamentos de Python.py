# Exercício de fundamentos de Python : Bibliotecas Pandas

# Exercício para praticar habilidades com Pandas, analisando o DataFrame Salaries

def msg (texto):
    print('--'*30)
    print(texto.center(60))
    print('--'*30)

import pandas as pd

sal = pd.read_csv('Salaries.csv', sep = ',')
msg('Head do DataFrame:')
print(sal.head(5))

msg('Informações sobre o DataFrame:')
print(sal.info())

msg('Média da coluna BasePay:')
print(sal['BasePay'].mean())

msg('Valor Máximo da OverTimePay :')
print(sal['OvertimePay'].max())

msg('Cargo do JOSEPH DRISCOLL :')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

msg('Salário com Benefícios do JOSEPH DRISCOLL :')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

msg('Pessoa mais bem paga incluindo os Benefícios :')
#print(sal[sal['TotalPayBenefits'] == ['TotalPayBenefits'].max()])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

msg('Pessoa menos bem paga incluindo os Benefícios :')
#print(sal[sal['TotalPayBenefits'] == ['TotalPayBenefits'].min()])
print(sal.loc[sal['TotalPayBenefits'].idxmin()])

msg('Média dos Salários por ano :')
print(sal.groupby('Year').mean()['BasePay'])

msg('Número de profissões:')
print(len(sal['JobTitle'].unique()))
#print(sal['JobTitle'].nunique()) # Outra forma

msg('As 5 profissões mais comuns:')
print(sal['JobTitle'].value_counts().head())
#print(sal['JobTitle'].value_counts().iloc[:5]) # Outra forma

msg('Número de pessoas com cargo único:')
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts()==1))

msg('Número de pessoas chefes:')
def chefe (title):
    if 'chief' in title.lower():
        return True
    else:
        return False
print(sum(sal['JobTitle'].apply(lambda x:chefe(x))))

msg('Existe uma relaçao trabalho salário:')
sal['Tamanho da String'] = sal['JobTitle'].apply(len)
print(sal[['Tamanho da String','TotalPayBenefits']].corr())
