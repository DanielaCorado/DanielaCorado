# Fundamentos de Python : Seaborn

# Nós estaremos trabalhando com conjunto de dados do Titanic
# Exercício para treinar as habilidades com Seaborn

def msg (texto):
    print('--'*30)
    print(texto.center(60))
    print('--'*30)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

msg('Head do DataFrame:')
print(titanic.head())

msg('Informações do DataFrame:')
print(titanic.info())

# Relação: age x fare
sns.jointplot(x='fare',y='age',data=titanic)
plt.show()

# Mostrar os dados de fare :
sns.displot(titanic['fare'], color='red',bins=30)
plt.show()

# Mostrar as classes dos passageiros com relação a idade:
sns.boxplot(x='class',y='age',data=titanic, palette='rainbow')
plt.show()

# Grafico de distribuição das classes com relaçao a idade:
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
plt.show()

# Divisão de acordo com sexo:
sns.countplot(x='sex',data=titanic)
plt.show()

# Mapa de calor dos dados:
corrtitanic = titanic.corr()
sns.heatmap(corrtitanic, cmap='coolwarm')
plt.title('Titanic Correlaçao')
plt.show()

# Relaão de idade e sexo em gráficos separados
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()
