# -*- coding: utf-8 -*-
import csv
from datetime import datetime

path_tipos = '../TipoProductos.csv'
path_productos = '../Productos.csv'
path_compras = '../Compras.csv'
path_ventas = '../Ventas.csv'

# Fernets
productos_a_analizar = [151, 476, 530]

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
    
    vta_pres_dia = {}
    ventas = {}

    for row in reader:
        # ventas ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo # aqui el precio es unitario
        sdia = row['Fecha']
        if sdia not in ventas.keys():
            ventas[sdia] = 0

        cantidad = int(row['Cantidad'])
        ventas[sdia] =+ cantidad

        dia = datetime.strptime(row['Fecha'], '%d/%m/%Y')
        dia_sem = dia.strftime('%A')

        idp = row['IDproducto']
        if int(idp) in productos_a_analizar:
            if dia_sem not in vta_pres_dia.keys():
                vta_pres_dia[dia_sem] = {idp: 0}
            if idp not in vta_pres_dia[dia_sem].keys():
                vta_pres_dia[dia_sem][idp] = 0

            vta_pres_dia[dia_sem][idp] += cantidad

for dia in vta_pres_dia.keys():

    print " ***************************** "
    print " {} ".format(dia)
    total = 0
    for idp in vta_pres_dia[dia].keys():
        total += vta_pres_dia[dia][idp]
        print " VENTA DE {}: {}".format(productos[idp]['nombre'], vta_pres_dia[dia][idp])
    print " VENTA TOTAL: {}".format(total)
        