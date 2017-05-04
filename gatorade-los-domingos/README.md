# Ventas de Gatorade por día de la semana

A [pedido de IACCanu](https://twitter.com/IACCancu/status/859941089297518592) aquí la venta de Gatorade por día. Teniendo [esta base de datos](https://github.com/avdata99/despensa-sierras-chicas/blob/master/README.md) es posible analizar.

## Análisis de ventas de Gatorade
Se analizan todas las ventas y se grupan po días

## Productos analizados según sus códigos en el sistema

### Códigos de productos Fernet
Basado en _Productos.csv_.  
 - 470,8,Gatorade bot 473 cc,"10,4005289078",13,No tiene
 - 636,8,Gatorade 1250 cc plastico,"23,8641643524",30,No tiene
 - 848,8,Gatorade 500 cc bot plastico,"11,2012643814",15,No Tiene


El script que analiza estos datos está [aquí](analyze.py).  
Los resultados son:  

```
 ***************************** 
 Saturday 
 VENTA DE Gatorade bot 473 cc: 220
 VENTA DE Gatorade 1250 cc plastico: 120
 VENTA DE Gatorade 500 cc bot plastico: 25
 VENTA TOTAL DE GATORADE: 365
 ***************************** 
 Tuesday 
 VENTA DE Gatorade bot 473 cc: 177
 VENTA DE Gatorade 1250 cc plastico: 121
 VENTA DE Gatorade 500 cc bot plastico: 24
 VENTA TOTAL DE GATORADE: 322
 ***************************** 
 Friday 
 VENTA DE Gatorade bot 473 cc: 190
 VENTA DE Gatorade 1250 cc plastico: 98
 VENTA DE Gatorade 500 cc bot plastico: 20
 VENTA TOTAL DE GATORADE: 308
 ***************************** 
 Monday 
 VENTA DE Gatorade bot 473 cc: 175
 VENTA DE Gatorade 1250 cc plastico: 103
 VENTA DE Gatorade 500 cc bot plastico: 10
 VENTA TOTAL DE GATORADE: 288
 ***************************** 
 Thursday 
 VENTA DE Gatorade bot 473 cc: 148
 VENTA DE Gatorade 1250 cc plastico: 114
 VENTA DE Gatorade 500 cc bot plastico: 12
 VENTA TOTAL DE GATORADE: 274
 ***************************** 
 Wednesday 
 VENTA DE Gatorade bot 473 cc: 144
 VENTA DE Gatorade 1250 cc plastico: 96
 VENTA DE Gatorade 500 cc bot plastico: 15
 VENTA TOTAL DE GATORADE: 255
 ***************************** 
 Sunday 
 VENTA DE Gatorade bot 473 cc: 154
 VENTA DE Gatorade 1250 cc plastico: 64
 VENTA DE Gatorade 500 cc bot plastico: 8
 VENTA TOTAL DE GATORADE: 226
```