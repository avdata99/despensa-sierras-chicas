# -*- coding: utf-8 -*-
"""
leer los archivos de base y producir otros más interesantes
"""
import csv

path_tipos = 'TipoProductos.csv'
path_productos = 'Productos.csv'
path_compras = 'Compras.csv'
path_ventas = 'Ventas.csv'

ventas = {}
for y in range(2008, 2016):
    for m in range(1, 13):
        mes = '%d-%s' % (y, str(m).zfill(2))
        ventas[mes] = 0

tipos ={}
with open(path_tipos) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tipos[row['ID2']] = {'nombre': row['TipoProducto'], 'compras': [], 'ventas': [], 'productos': []}

# print str(tipos)

productos = {}
with open(path_productos) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ID,IdTipoProducto,nProducto,pCosto,pVenta,CodEnvase
        # ignoro costo y precio de venta porque puede estar desactualizado
        nombre = row['nProducto']
        if row['CodEnvase'] != 'No tiene':
            nombre += ' ('+row['CodEnvase']+')'
            
        productos[row['ID']] = {'tipo': row['IdTipoProducto'], 
                                'nombre': nombre, 
                                'compras': [], 
                                'ventas': [],
                                'ventas_mensuales': ventas.copy(), # cantidad de unidades vendidas por mes
                                'precios_mensuales': ventas.copy() # precios de cada mes
                                }

        tipos[row['IdTipoProducto']]['productos'].append(row['ID'])

# print str(productos)

with open(path_compras) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # compras ID,Fecha,IDproducto,Cantidad,PrecioTotal
        precio_total = float(row['PrecioTotal'].replace(',', '.'))
        cantidad = float(row['Cantidad'])
        producto = productos[row['IDproducto']]
        compra = {'fecha': row['Fecha'], 'cantidad': cantidad, 'precio': precio_total/cantidad }
        producto['compras'].append(compra)
        tipos[producto['tipo']]['compras'].append(compra)

with open(path_ventas) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ventas ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo # aqui el precio es unitario
        precio = float(row['Precio'].replace(',', '.'))
        cantidad = float(row['Cantidad'])
        producto = productos[row['IDproducto']]
        venta = {'fecha': row['Fecha'], 'cantidad': cantidad, 'precio': precio }
        producto['ventas'].append(venta)
        tipos[producto['tipo']]['ventas'].append(venta)
        dia, mes, ano = row['Fecha'].split('/')
        m = '%s-%s' % (ano, mes)
        producto['ventas_mensuales'][m] = producto['ventas_mensuales'][m] + cantidad
        if precio > 0:
            producto['precios_mensuales'][m] = precio/cantidad # toma una cualquiera del mes
        

# exportar
from slugify import slugify

for p, producto in productos.iteritems():

    prod = slugify(producto['nombre'].decode('utf-8'))
    tipo = slugify(tipos[producto['tipo']]['nombre'].decode('utf-8'))
    tipo_id = producto['tipo']
    
    if len(producto['compras']) > 0:
        fname = 'data/compras_prod_%s.csv' % p
        with open(fname, 'w') as csvfile:
            fieldnames = producto['compras'][0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
            writer.writeheader()
            for compra in producto['compras']:
                writer.writerow(compra)

    if len(producto['ventas']) > 0:
        fname = 'data/ventas_prod_%s.csv' % p
        with open(fname, 'w') as csvfile:
            fieldnames = producto['ventas'][0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
            writer.writeheader()
            for venta in producto['ventas']:
                writer.writerow(venta)

# variedad de ventas de productos por tipo y cantidad
for t, tipo in tipos.iteritems():
    tipo_nombre = slugify(tipo['nombre'].decode('utf-8'))

    fname = 'data/tipo_%s_ventas.csv' % tipo_nombre
    with open(fname, 'w') as csvfile:
        fieldnames = ['producto'] + sorted(ventas.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for p in tipo['productos']:
            prod = productos[p]
            row = {'producto': prod['nombre']}
            row.update(prod['ventas_mensuales'])
            writer.writerow(row)


    fname = 'data/tipo_%s_precio.csv' % tipo_nombre
    with open(fname, 'w') as csvfile:
        fieldnames = ['producto'] + sorted(ventas.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for p in tipo['productos']:
            prod = productos[p]
            row = {'producto': prod['nombre']}
            row.update(prod['precios_mensuales'])
            writer.writerow(row)