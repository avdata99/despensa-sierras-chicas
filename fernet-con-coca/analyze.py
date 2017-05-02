# -*- coding: utf-8 -*-
"""
cruzar datos de ventas en un mismo ticket de fernets y coca
"""
import csv
from datetime import datetime

path_tipos = '../TipoProductos.csv'
path_productos = '../Productos.csv'
path_compras = '../Compras.csv'
path_ventas = '../Ventas.csv'

# Fernets
productos_a_analizar_1 = [327, 328, 329, 330, 331, 463, 598,
                        646, 784, 334, 337, 338, 339, 340]

# Cocas 
productos_a_analizar_2 = [118, 119, 121, 122, 471]

# tomar datos de los IDs descriptos
productos = {}
with open(path_productos) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ID,IdTipoProducto,nProducto,pCosto,pVenta,CodEnvase
        # ignoro costo y precio de venta porque puede estar desactualizado
        idp = row['ID']
        if int(idp) in productos_a_analizar_1 + productos_a_analizar_2:
            nombre = row['nProducto']
            productos[idp] = {'nombre': nombre}


with open(path_ventas) as csvfile:
    reader = csv.DictReader(csvfile)
    idventa = 0
    tiene_productos_1 = False
    tiene_productos_2 = False

    vta_coca_sin_fernet = {}
    vta_coca_con_fernet = {}

    ventas_interesantes_finales = []  # ventas que tiene de uno o los dos tipos

    for row in reader:
        # ventas ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo # aqui el precio es unitario
        # dia, mes, ano = row['Fecha'].split('/')
        dia = datetime.strptime(row['Fecha'], '%d/%m/%Y')
        dia_sem = dia.strftime('%A')

        # agrupar las cosas por ventas
        if idventa != row["IDVenta"]:
            if tiene_productos_2:
                if not tiene_productos_1:
                    if dia_sem not in vta_coca_sin_fernet.keys():
                        vta_coca_sin_fernet[dia_sem] = 1
                    else:
                        vta_coca_sin_fernet[dia_sem] += 1
                    
                else:
                    if dia_sem not in vta_coca_con_fernet.keys():
                        vta_coca_con_fernet[dia_sem] = 1
                    else:
                        vta_coca_con_fernet[dia_sem] += 1
                    
                    ventas_interesantes_finales.append(productos_mezclados)

            productos_mezclados = []  # ids de los productos mezclados en esta venta
            tiene_productos_1 = False
            tiene_productos_2 = False
            productos_en_esta_venta = []
            idventa = row["IDVenta"]

        idp = row['IDproducto']
        if int(idp) in productos_a_analizar_1:
            tiene_productos_1 = True
            productos_mezclados.append(int(idp))

        if int(idp) in productos_a_analizar_2:
            tiene_productos_2 = True
            productos_mezclados.append(int(idp))


        #if tiene_productos_1 or tiene_productos_2:
        #    producto = productos[idp]

        # m = '%s-%s' % (ano, mes)
        
# % de coca con fernet 
for dia in vta_coca_con_fernet.keys():

    porc_sin_fernet = 100.0 * vta_coca_con_fernet[dia] / (vta_coca_sin_fernet[dia] + vta_coca_con_fernet[dia])
    print " ***************************** "
    print " {} ".format(dia)
    print " VENTA DE COCA SIN FERNET: {} ".format(vta_coca_sin_fernet[dia])
    print " VENTA DE COCA CON FERNET: {} ".format(vta_coca_con_fernet[dia])
    print " % de venta de COCA CON FERNET: {} ".format(porc_sin_fernet)
    