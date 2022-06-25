
import pandas as pd
import matplotlib as plt


base = pd.read_excel('RC-RecebidasAbandonadas.xlsx')

# type(base)
#
# print(type(base))
#
# base.head(21)
#
# print(base.head(13))
#
# print(base.dtypes)

# print(base[base['Grupo'] == "SaoCristovao"])
#
# base.plot.scatter(x='Grupo', y='Tempo de Espera')

print(base["Tempo de Espera"].mean())

print(base["Tempo de Espera"].describe())

