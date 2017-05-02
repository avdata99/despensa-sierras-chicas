# Análisis de ventas de Coca Cola con o sin fernet

Mi hijo me dijo que al menos un cuarto de las cocas que se venden son para Fernet.  
Teniendo [esta base de datos](https://github.com/avdata99/despensa-sierras-chicas/blob/master/README.md) es posible ver si es así.

## Análisis de ventas conjuntas de Coca (2 o mas lts) con o sin Fernet (Branca u otros)
Se analizan todas las ventas y se marcan aquellas que tienen o no Coca Cola y opcionalmente Fernet (Cualquier marca).  

## Productos analizados según sus códigos en el sistema

### Códigos de productos Fernet
Basado en _Productos.csv_.  
 - 327,9,Fernet Branca 1/2 l,"51,5066299438",65,No tiene
 - 328,9,Fernet Branca 3/4,"79,8821563721",96,No tiene
 - 329,9,Fernet Branca ESTUCHE +VASO,"135,0017242432",165,No tiene
 - 330,9,Fernet Branca menta 3/4,"67,8613052368",96,No tiene
 - 331,9,Fernet Branca mini,"11,5167236328",13,No tiene
 - 463,9,Fernet Branca menta 1/2 lt,"35,7009162903",65,No tiene
 - 598,9,Fernet Branca RETRO 3/4,"89,5011444092",108,No tiene
 - 646,9,Fernet Cazalis 750 cc,"4,2300000191",7,No tiene
 - 784,9,Fernet Ramazzoti,"14,7700004578",17,No tiene
 - 334,9,Fernet 1882,"56,5417938232",68,No tiene
 - 337,9,Fernet 1882 chico,"33,0197906494",40,No tiene
 - 338,9,Fernet Porta,"6,1999998093","7,5",No tiene
 - 339,9,Fernet Vittone 1/2 l,"16,5005321503",20,No tiene
 - 340,9,Fernet Vittone 1lt,"31,9060382843",40,No tiene


### Códigos de la Coca Cola
Basado en _Productos.csv_.  
 - 118,7,Coca 2250cc desc,"23,5969944",32,No tiene
 - 119,7,Coca 2l ret,"15,9736766815",20,Coca 2l
 - 121,7,Coca 2500 cc ret GRANDE NUEVA,"20,842962265",25,No tiene
 - 122,7,Coca 1500 c.c. desc,"16,94739151",22,No tiene
 - 471,7,Coca 2500cc descartable,"27,4173412323",33,No tiene
* algunas cocas mas chicas no se usan 

Como varíá mucho entre díás el resultado del análisis da resultados por día de la semana.  
El script que analiza estos datos está [aquí]().  
Los resultados son:  

```
 ***************************** 
 Monday 
 VENTA DE COCA SIN FERNET: 4614 
 VENTA DE COCA CON FERNET: 369 
 % de venta de COCA CON FERNET: 7.40517760385 
 ***************************** 
 Tuesday 
 VENTA DE COCA SIN FERNET: 4750 
 VENTA DE COCA CON FERNET: 402 
 % de venta de COCA CON FERNET: 7.80279503106 
 ***************************** 
 Friday 
 VENTA DE COCA SIN FERNET: 8971 
 VENTA DE COCA CON FERNET: 1971 
 % de venta de COCA CON FERNET: 18.0131602998 
 ***************************** 
 Wednesday 
 VENTA DE COCA SIN FERNET: 5090 
 VENTA DE COCA CON FERNET: 550 
 % de venta de COCA CON FERNET: 9.75177304965 
 ***************************** 
 Thursday 
 VENTA DE COCA SIN FERNET: 5198 
 VENTA DE COCA CON FERNET: 607 
 % de venta de COCA CON FERNET: 10.4565030146 
 ***************************** 
 Sunday 
 VENTA DE COCA SIN FERNET: 8803 
 VENTA DE COCA CON FERNET: 1105 
 % de venta de COCA CON FERNET: 11.1526039564 
 ***************************** 
 Saturday 
 VENTA DE COCA SIN FERNET: 12536 
 VENTA DE COCA CON FERNET: 3229 
 % de venta de COCA CON FERNET: 20.4820805582 
 ```

* No uso estas cocas:  
 - 13,7,Lata Coca linea,"6,6671676636",8,Cerveza
 - 120,7,Coca light 2l ret,"15,0024938583",20,Coca 2l
 - 124,7,Coca 500 c.c desc,"8,1532125473",10,No tiene
 - 123,7,Coca vidrio,"12,5001716614",15,Coca 1 1/4 l
 - 125,7,Coca 1 lt,"13,3332643509",16,No tiene
 - 126,7,Coquitas,"4,3713417053",6,No tiene
 - 544,7,Coca Light 500cc desc,"6,3001737595",10,No tiene
 - 569,7,Coca Light 1500CC desc,"17,3827838898",22,No tiene
 - 694,7,Coca LIFE 1500cc,"14,1667003632",20,No tiene
 - 742,7,Coca Zero 2250cc,"25,234910965",32,No tiene
 - 856,7,Coca Zero Vidrio,"12,4999294281",15,No Tiene
 - 131,7,Coca zero 1500cc desc,"18,333032608",22,No tiene
 - 134,7,Coca Zero 2l ret,"16,3267383575",20,No tiene
 - 332,7,Coca Zero 500 cc,"8,1362447739",10,No tiene
 - 409,7,coca 1000 ret vieja,"6,2503175735","4,75",No tiene
 