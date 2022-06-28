
import pandas as pd
import matplotlib as plt


base = pd.read_excel('RC-RecebidasAbandonadas.xlsx')

# type(base)
#
# print(type(base))
#
# base.head(21)

# display(base)
# print(base.head(13))
#
# print(base.isnull().sum()) # pode ser usado para contar os nulos
#
grupo = base["Grupo"]
# print(grupo.value_counts())


#
# print(base.dtypes)

# print(base[base['Grupo'] == "SaoCristovao"])
#
# base.plot.scatter(x='Grupo', y='Tempo de Espera')

# print(base["Tempo de Espera"].mean())
#
# print(base["Tempo de Espera"].describe())



base_estatistica = [['Grupo', grupo.value_counts()]]

print(base_estatistica)