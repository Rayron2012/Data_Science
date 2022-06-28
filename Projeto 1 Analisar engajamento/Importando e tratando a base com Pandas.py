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

print(base)