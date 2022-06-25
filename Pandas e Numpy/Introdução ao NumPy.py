'''
NumPy
Ele é a "base" para o Pandas

Numerical Python
Biblioteca de computação numérica
Otimizada para cálculos pesados
https://numpy.org/

No NumPy vamos trabalhar com arrays, que são mais rápidos e mais performáticos que listas'''

# Importar o numpy
import numpy as np

'''Vamos supor que temos a venda e comissão (em percentual) de 5 vendedores e queremos saber qual vai ser o salário de cada um deles'''

# Venda e comissão
venda_valor = [150000,230000,82000,143000,184000]
comissao = [5,8,8,5,12]

# print(venda_valor*(comissao/100))
# Da forma acima da erro pois normalmente essa conta é pesada para concpletar dessa forma

'''--------------------------------------------------------------------------------------------'''
# Transformar uma lista em um array:

venda_valor = np.array(venda_valor)
comissao = np.array(comissao)

# Agora vamos conseguir fazer sendo um array
print(venda_valor*(comissao/100))

# Dimensões de um array
'''meu_array.shape'''
print(venda_valor.shape)

# Dados de :https://colab.research.google.com/drive/1m7cGwUe1cdk2FNCd_x3eUIg_F-pgX_oQ#scrollTo=e3a4bfe9
