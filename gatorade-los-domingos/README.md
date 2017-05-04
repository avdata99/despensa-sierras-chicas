# Ventas de Gatorade por día de la semana

A [pedido de IACCanu](https://twitter.com/IACCancu/status/859941089297518592) aquí la venta de Gatorade por día. Teniendo [esta base de datos](https://github.com/avdata99/despensa-sierras-chicas/blob/master/README.md) es posible analizar.

## Análisis de ventas de Gatorade
Se analizan todas las ventas y se grupan po días

## Productos analizados según sus códigos en el sistema

### Códigos de productos Fernet
Basado en _Productos.csv_.  
 - 470,8,Gatorade bot 473 cc
 - 636,8,Gatorade 1250 cc plastico
 - 848,8,Gatorade 500 cc bot plastico


El script que analiza estos datos está [aquí](analyze.py).  
Los resultados son:  

```
***************************** 
Monday 
VENTA DE Gatorade bot 473 cc: 219
VENTA DE Gatorade 1250 cc plastico: 109
VENTA DE Gatorade 500 cc bot plastico: 16
VENTA TOTAL DE GATORADE: 344
***************************** 
Tuesday 
VENTA DE Gatorade bot 473 cc: 194
VENTA DE Gatorade 1250 cc plastico: 128
VENTA DE Gatorade 500 cc bot plastico: 27
VENTA TOTAL DE GATORADE: 349
***************************** 
Friday 
VENTA DE Gatorade bot 473 cc: 223
VENTA DE Gatorade 1250 cc plastico: 102
VENTA DE Gatorade 500 cc bot plastico: 23
VENTA TOTAL DE GATORADE: 348
***************************** 
Wednesday 
VENTA DE Gatorade bot 473 cc: 166
VENTA DE Gatorade 1250 cc plastico: 102
VENTA DE Gatorade 500 cc bot plastico: 16
VENTA TOTAL DE GATORADE: 284
***************************** 
Thursday 
VENTA DE Gatorade bot 473 cc: 182
VENTA DE Gatorade 1250 cc plastico: 121
VENTA DE Gatorade 500 cc bot plastico: 14
VENTA TOTAL DE GATORADE: 317
***************************** 
Sunday 
VENTA DE Gatorade bot 473 cc: 176
VENTA DE Gatorade 1250 cc plastico: 77
VENTA DE Gatorade 500 cc bot plastico: 8
VENTA TOTAL DE GATORADE: 261
***************************** 
Saturday 
VENTA DE Gatorade bot 473 cc: 267
VENTA DE Gatorade 1250 cc plastico: 126
VENTA DE Gatorade 500 cc bot plastico: 33
VENTA TOTAL DE GATORADE: 426
```