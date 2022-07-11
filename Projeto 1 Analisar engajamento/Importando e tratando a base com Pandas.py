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

# print(base.groupby(['Tipo', 'Pessoas', 'Campanhas'])[["Curtidas", "Comentários"]].mean())
'''Nessa estrutura a com mais de uma coluna temos que utilizar [] dentro de parenteses, para declarar mais de um argumento,
e no segundo parametro de quantidade colocar [[dento]] colocar Colchetes dentro de Colchetes'''

# print(base.groupby('Pessoas')[["Curtidas", "Comentários"]].mean())
"""Aqui tiramos a prova que as publicações mais curtidas são as que contém pessoas!"""

# print(base[base.Tipo == 'Foto'].groupby("Carrossel")[["Curtidas", "Comentários"]].mean())
'''Aqui vemos que analisando apenas carrosel de fotos não temos tantas interações como pensavamos'''

# print(base.groupby(['Pessoas', 'Campanhas'])[["Curtidas", "Comentários"]].mean())
'''Nesse casopodemos perceber que as melhores publicações são as que possuem pessoas e as que possuem campanhas'''

# print(base[base.Tipo == "Vídeo"])

data = base[base.Tipo == "Vídeo"]
print(data)

'''Analisando este cenario podemos identificar que de acordo com os dados, a média de video foi positiva e o que esta'''

'''Nesse caso podemos sugerir que a marca continue fazendo vídeos com posseoas e/ou em épocas de campanhas pois tem o 
maior engajamento'''

'''Para analisar a linha do tempo retirar o # do comentario, para conseguir analisar todos os passos individualmente!'''

