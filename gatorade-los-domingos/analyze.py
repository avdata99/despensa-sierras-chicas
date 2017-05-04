# -*- coding: utf-8 -*-
import csv
from datetime import datetime

path_tipos = '../TipoProductos.csv'
path_productos = '../Productos.csv'
path_compras = '../Compras.csv'
path_ventas = '../Ventas.csv'

# Fernets
productos_a_analizar = [470, 636, 848]

# tomar datos de los IDs descriptos
productos = {}
with open(path_productos) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ID,IdTipoProducto,nProducto,pCosto,pVenta,CodEnvase
        # ignoro costo y precio de venta porque puede estar desactualizado
        idp = row['ID']
        if int(idp) in productos_a_analizar:
            nombre = row['nProducto']
            productos[idp] = {'nombre': nombre}


with open(path_ventas) as csvfile:
    reader = csv.DictReader(csvfile)
    
    vta_gatorade = {}
    
    for row in reader:
        # ventas ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo # aqui el precio es unitario
        # dia, mes, ano = row['Fecha'].split('/')
        dia = datetime.strptime(row['Fecha'], '%d/%m/%Y')
        dia_sem = dia.strftime('%A')

        idp = row['IDproducto']
        if int(idp) in productos_a_analizar:
            if dia_sem not in vta_gatorade.keys():
                vta_gatorade[dia_sem] = {idp: 0}
            if idp not in vta_gatorade[dia_sem].keys():
                vta_gatorade[dia_sem][idp] = 0

            cantidad = int(row['Cantidad'])
            vta_gatorade[dia_sem][idp] += cantidad

for dia in vta_gatorade.keys():

    print " ***************************** "
    print " {} ".format(dia)
    total = 0
    for gato in vta_gatorade[dia].keys():
        total += vta_gatorade[dia][gato]
        print " VENTA DE {}: {}".format(productos[gato]['nombre'], vta_gatorade[dia][gato])
    print " VENTA TOTAL DE GATORADE: {}".format(total)
        