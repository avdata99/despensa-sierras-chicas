# Precios, compras y ventas 
En una despensa de Sierras Chicas (Córdoba, Argentina).  
Datos 2008/2015 de ventas por tipos de productos de un comercio de bebidas de Sierras Chicas - Córdoba.  

Los datos de base son los CSVs Productos y TipoProductos.  
Por suerte el sistema esta organizado por tispo (aunque algunos productos no estan bien catalogados).  
Todas las compras y ventas de productos estan en CSVs separados.  

El archivo **analyze.py** es una primera pasada por los datos para generar nuesvos CSVs específicos.  
No esta terminado pero los datos puede servir para hacer una linda mini app para mirar datos.  

Las ventas tiene un detalle interesante, tiene un ID de venta por lo que puede 
saberse que *combos* de productos llevan los clientes.  

En las ventas estan tambien el costo estimado del producto, esto puede decir que margen de ganacia hay.  
Los precios pueden servir para una evolución de precios (no para medir inflación! OJO).  
