'''
Desafio:

Analisando o engajamento do Instagram
O que queremos responder?
Qual tipo de conteúdo mais engaja no Instagram da minha empresa?

Temos a base de dados do Instagram desde que o usuário começou a postar na marca até o dia 27/março

Ele também dá alguns direcionamentos:
Podem ignorar a coluna visualizações, queremos entender apenas curtidas, comentários e interações
Tags vazias é que realmente não possuem tag (favor tratar como vazio)'''

#  importar a base com pandas
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_excel("08. Analisando o engajamento no Instagram.xlsx")

# Retirar a coluna visualizações
base = base.drop('Visualizações', axis=1)

# print(base.loc[base.Carrossel.isnull()].head())
'''Loc localiza valores, codar com a estrutura acima'''

# print(base.loc[base.Carrossel.notnull()].head())
'''localizar valores não nulos'''

# print(base.Carrossel.value_counts())
'''Contar valores em uma coluna, mostra gistros dessas linhas e quantidades'''

base.loc[base.Carrossel.isnull(),"Carrossel"] = "N"
'''Subistitui os valores filtrados por N'''

# print(base.describe())
'''Descrimina a base de acordo com parametros'''

# print(base.plot(kind="scatter", x="Data", y="Curtidas", figsize=(14,8)))

# print(base.sort_values(by="Curtidas", ascending=False).head())
'''sort_values, ordena o valor, e o by seleciona a coluna'''

base.groupby('Tipo')["Curtidas"].mean()
'''Estrutura : após o groupby, inserir a categoria que quer agrupar e entre colchetes a informação que deseja que seja 
agrupada, e no final a função de agregação'''


print(base.groupby('Tipo')["Curtidas"].mean())

