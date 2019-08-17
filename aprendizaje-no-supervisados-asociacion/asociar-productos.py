
# ## Aprendizaje de reglas de asociación

# Objetivo:
#     
#     derivar reglas de la forma {A} -> {B}
#     
# copiado de acá: https://github.com/DiploDatos/AprendizajeNOSupervisado/blob/master/Reglas_de_Asoc_demo1.ipynb

import pandas as pd
import numpy as np
import sys
from itertools import combinations, groupby
from collections import Counter
from IPython.display import display


# Descripcion de los datos:
# 
# Ventas.csv
""" 
ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo
45830,A-0001-00001162,01/07/2007,277,2,3,"2,4100000858"
45831,A-0001-00001162,01/07/2007,71,1,"3,75","3,4600000381"
45832,A-0001-00001162,01/07/2007,814,1,8,"6,5999999046"
45833,A-0001-00001162,01/07/2007,6,2,"3,25","2,7000000477"
"""

# 
# Productos.csv
"""
ID,IdTipoProducto,nProducto,pCosto,pVenta,CodEnvase
877,10,Corona 710 cc,"36,8732032776",50,No Tiene
878,13,Serie Terra,"38,8547668457",48,No Tiene
879,10,Reaktor energizante Reactor,"7,5",10,No Tiene
880,13,Baron del Plata,"2,2712545395",3,No Tiene
881,13,Alma Mora,"38,4314918518",50,No Tiene
882,13,Finca Beltran Duo,"6,5999999046",8,No Tiene
883,7,Seven Free 2250cc oferta,"23,3419036865",30,No Tiene
884,10,Encendedor Magiclick,"5,0513253212",6,No Tiene
885,4,Red Point,"9,9679584503",14,No Tiene
"""

# TipoProductos.csv 
"""
ID2,TipoProducto
1,Aguas - Sodas
2,Cerveza
3,Champ-Sidras-Espumantes
4,Cigarrillos
5,Cocteles
6,Envases
7,Gaseosas
8,Jugos - Amargos
"""

def size(obj):
    return "{0:.2f} MB".format(sys.getsizeof(obj) / (1000 * 1000))

path_ventas = ''
orders = pd.read_csv('../Ventas.csv')
print('orders -- dimensions: {0};   size: {1}'.format(orders.shape, size(orders)))
display(orders.head())
items_names = pd.read_csv('../Productos.csv')
display(items_names.head())

items_type_names = pd.read_csv('../TipoProductos.csv')
display(items_type_names.head())

# agregar el tipo de producto a la tabla de productos
item_and_types = pd.merge(items_names[['ID','IdTipoProducto', 'nProducto']],
                      items_type_names[['ID2','TipoProducto']],
                      left_on='IdTipoProducto',
                      right_on='ID2',
                      how='inner')

# decodificar el nombre de los productos
compras_df = pd.merge(orders[['IDVenta','IDproducto']],
                      # items_names[['ID','nProducto']],  # aqui es para hacer por productos (da muy poco)
                      item_and_types[['ID', 'IdTipoProducto', 'TipoProducto']],
                      left_on='IDproducto',
                      right_on='ID',
                      how='inner')



print('----------------Compras DF------------------------')
# aca es con productos directo, da poco
# compras_df = compras_df[['IDVenta', 'IDproducto', 'nProducto']]
compras_df = compras_df[['IDVenta', 'IdTipoProducto', 'TipoProducto']]

display(compras_df.head())
compras_df=compras_df.sort_values(by='IDVenta',
                                  axis=0,
                                  ascending=True,
                                  inplace=False,
                                  kind='quicksort',
                                  na_position='last')
compras=compras_df.values[:,[0,2]]
print(compras)

transactions=[]
for orders_id, order_object in groupby(compras, lambda x: x[0]):
    transactions.append([item[1] for item in order_object])
print('------------- Transacciones (solo algunas) -----------------')
print(transactions[:20])

# con toda la base..
# IOPub data rate exceeded.
# The notebook server will temporarily stop sending output


from efficient_apriori import apriori
# wARNING-CUIDADO!! no poner min_support pequeño como por ejempo 0.001!!
# min_support y min_confiden entre 0 y 1
min_support = 0.01
min_confidence = 0.3
itemsets, rules = apriori(transactions, min_support=min_support,  min_confidence=min_confidence)

print(f'------------- RULES Support:{min_support} Confidence:{min_confidence}-----------------')
#rules = filter(lambda rule: len(rule.lhs) == 2 and len(rule.rhs) == 1, rules)
rules=sorted(rules, key=lambda rule: rule.confidence)
for rule in rules:
  print(rule) # Prints the rule and its confidence, support, lift, ...

