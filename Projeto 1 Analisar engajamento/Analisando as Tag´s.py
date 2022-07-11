import pandas as pd

base = pd.read_excel("08. Analisando o engajamento no Instagram.xlsx")

base = base.drop('Visualizações', axis=1)

# print(base.head())

base.groupby('Tags')["Curtidas"].mean()

# print(base.groupby('Tags')["Curtidas"].mean())
'''Vemos que existem tags mais de uma vez, porém não são tag´s exclusivas'''

'''Utilizar o split na coluna ajuda a separar os valores, para isso devo acessar a coluna diretasmente e fazer um
tratamento por "/"'''

base.Tags = base.Tags.str.split("/")


# /////////////////////////////////////////////////////////////
dic = {
    'A': [[1, 2], 3, [4, 5, 6], []],
    "B": [1, 2, 3, 4],
}
base_dic = pd.DataFrame(dic)
'''Transformar sempre em dataframe (tabela)'''

base_dic = base_dic.explode("A")
# print(base_dic)

'''No exemplo acima utilizamos o explode que na coluna 'A', tudo que esta em lista sera separado e em uma linha por elemento
 e o que não estiver sera mantido.
As demais colunas irão duplicar seus valores e o indice também será repetido'''
 # //////////////////////////////////////////////////////////

base = base.explode('Tags')

"""Toda vez que utilizar explode só podera efetuar analise daquela coluna do explodo pois ela duplicara os demais valores"""

"""base.groupby("Pessoas")['Curtidas'].mean() essa esta errada pois duplicaria os valores da coluna pessoa"""

base.groupby("Tags")[["Curtidas","Comentários"]].mean().sort_values("Curtidas",ascending=False) #.to_numeric(s, downcast='float')

base.loc[base.Tags.isnull(),"Tags"] = 'Sem Tag'

print(base.groupby("Tags")[["Curtidas", "Comentários"]].mean().sort_values("Curtidas", ascending=False))
print()

'''Desse jeito temos as visões por tags, ficando mais facil de nosso cliente analisar por tags o que mais foi curtido e comentado
incluirndo o que estiver sem tag, sendo curtidas aleatorias sem campanhas'''

"""Para voltar ao normal com os valuroes nulos: """

import numpy as np

base.loc[base.Tags== 'Sem Tag', 'Tags'] = np.nan

print(base.groupby("Tags")[["Curtidas", "Comentários"]].mean().sort_values("Curtidas",ascending=False))
print()

'''Analise de pessoas e tags'''

print(base.groupby(['Pessoas',"Tags"])[["Curtidas", "Comentários"]].mean().sort_values("Curtidas",ascending=False))
print()

'''Analise de Campanhas e tags'''

print(base.groupby(['Campanhas',"Tags"])[["Curtidas", "Comentários"]].mean().sort_values("Curtidas",ascending=False))
print()

"Consclusões" \
"" \
"Ter rostos de outras pessoas é fundamental para as curtidas e visualizações" \
"Criar campanhas é muito importante para a marca" \
"Influenciadores é importante em epocas de campanhas" \
"Promoções teve um maior desempenho que qualquer outra tag, sabemos que com promoções o alcance é maior" \
"Usar conteudos en trend ajuda na divulgação da marca, mesmo sendo de outros nichos" \
"A melhor maneira de usar produtos é com outras pessoas os usando " \
"Para inclusão de novos produtos é super importante a participação de pessoas utilizando" \
"Continuarei testando ostras tags com e sem campanhas/pessoas para afunilar ainda mais os testes."""
