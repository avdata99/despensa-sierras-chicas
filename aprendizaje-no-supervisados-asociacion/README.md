# Reglas de asociaciones

Asociación por productos o (mejor) por categorías de productos.  

## Por categorías

```
python3 asociar-categorias.py
------------- RULES Support:0.01 Confidence:0.3-----------------

           GANADOR
{Licores - Fernet - etc} -> {Gaseosas} (conf: 0.611, supp: 0.037, lift: 1.519, conv: 1.536)
           A.K.A: Fernet con Coca

{Cigarrillos, Vino Tetra} -> {Gaseosas} (conf: 0.334, supp: 0.010, lift: 0.831, conv: 0.898)
{Otros} -> {Gaseosas} (conf: 0.335, supp: 0.020, lift: 0.833, conv: 0.899)
{Cerveza} -> {Gaseosas} (conf: 0.340, supp: 0.062, lift: 0.845, conv: 0.905)
{Aguas - Sodas} -> {Gaseosas} (conf: 0.344, supp: 0.032, lift: 0.857, conv: 0.912)
{Cerveza, Cigarrillos} -> {Gaseosas} (conf: 0.360, supp: 0.013, lift: 0.896, conv: 0.935)
{Vino 3/4} -> {Gaseosas} (conf: 0.363, supp: 0.043, lift: 0.903, conv: 0.939)
{Vino Tetra} -> {Gaseosas} (conf: 0.370, supp: 0.043, lift: 0.919, conv: 0.949)
{Extras} -> {Gaseosas} (conf: 0.533, supp: 0.031, lift: 1.325, conv: 1.279)
```

Estos son las categorías de productos:

ID2,TipoProducto
 - -1,Extras
 - 1,Aguas - Sodas
 - 2,Cerveza
 - 3,Champ-Sidras-Espumantes
 - 4,Cigarrillos
 - 5,Cocteles
 - 6,Envases
 - 7,Gaseosas
 - 8,Jugos - Amargos
 - 9,Licores - Fernet - etc
 - 10,Otros
 - 11,Promociones
 - 12,Tarjetas
 - 13,Vino 3/4
 - 14,Vino Botella
 - 15,Vino Damajuana
 - 16,Vino Tetra


## Por productos

```
python3 asociar-productos.py

------------- RULES Support:0.001 Confidence:0.001-----------------

# Gancia con Sprite
{Americano Gancia 930cc} -> {Sprite 2250cc desc} (conf: 0.261, supp: 0.002, lift: 32.406, conv: 1.342)

# Fernet con Coca
{Fernet Branca 3/4} -> {Coca 2l ret} (conf: 0.368, supp: 0.007, lift: 3.142, conv: 1.397)
{Fernet Branca 1/2 l} -> {Coca 2l ret} (conf: 0.319, supp: 0.004, lift: 2.726, conv: 1.297)
{Fernet Branca 3/4} -> {Coca 2250cc desc} (conf: 0.226, supp: 0.005, lift: 8.952, conv: 1.259)
{Fernet Branca 1/2 l} -> {Coca 2250cc desc} (conf: 0.206, supp: 0.002, lift: 8.164, conv: 1.228)
{Fernet Branca 3/4} -> {Coca 2500 cc ret GRANDE NUEVA} (conf: 0.077, supp: 0.002, lift: 3.831, conv: 1.061)

# Sodeado
{Toro Tinto tetra} -> {Soda Sifon Manaos} (conf: 0.044, supp: 0.002, lift: 3.517, conv: 1.033)
{Toro Tinto tetra} -> {Soda La moderna 1 1/2  lts} (conf: 0.043, supp: 0.002, lift: 4.967, conv: 1.036)
{Carragal tto} -> {Soda Bichy} (conf: 0.071, supp: 0.001, lift: 3.714, conv: 1.056)
{Soda Bichy} -> {Toro Tinto tetra} (conf: 0.183, supp: 0.004, lift: 3.790, conv: 1.165)
{Toro Blanco tetra} -> {Soda Bichy} (conf: 0.062, supp: 0.001, lift: 3.222, conv: 1.046)

# Prittyau
{Pritty 2 1/4 l} -> {Toro Tinto tetra} (conf: 0.166, supp: 0.005, lift: 3.429, conv: 1.141)
{Pritty 2 1/4 l} -> {Balbo Magnum} (conf: 0.044, supp: 0.001, lift: 2.281, conv: 1.026)

# Indeciso
{Toro Tinto tetra} -> {Toro Blanco tetra} (conf: 0.042, supp: 0.002, lift: 2.343, conv: 1.025)
{Coca 2l ret} -> {Fanta 2l ret} (conf: 0.028, supp: 0.003, lift: 2.148, conv: 1.016)
{Coca 2l ret} -> {Sprite 2l ret y zero 2l ret} (conf: 0.034, supp: 0.004, lift: 2.290, conv: 1.020)

#### Que????
{Don Ernesto tinto tetra} -> {Richmond} (conf: 0.442, supp: 0.002, lift: 40.388, conv: 1.773)

#### Cheto
{Sta Florentina Bivarietales} -> {Coca light 2l ret} (conf: 0.108, supp: 0.001, lift: 9.262, conv: 1.109)

{Quilmes} -> {Fanta 2l ret} (conf: 0.027, supp: 0.001, lift: 2.088, conv: 1.015)

{Toro Tinto tetra} -> {Camel 20} (conf: 0.021, supp: 0.001, lift: 2.856, conv: 1.014)
{Toro Tinto tetra} -> {Rodeo} (conf: 0.024, supp: 0.001, lift: 2.579, conv: 1.015)

{Brahma} -> {Richmond} (conf: 0.028, supp: 0.002, lift: 2.601, conv: 1.018)
{Toro Tinto tetra} -> {Hook Cola x 2 1/4 lt} (conf: 0.029, supp: 0.001, lift: 2.008, conv: 1.015)


{Coca 2250cc desc} -> {Sprite 2250cc desc} (conf: 0.050, supp: 0.001, lift: 6.264, conv: 1.045)
{Toro Blanco tetra} -> {Soda Sifon Manaos} (conf: 0.088, supp: 0.002, lift: 7.003, conv: 1.083)
{Coca 2250cc desc} -> {Balbo Magnum} (conf: 0.045, supp: 0.001, lift: 2.350, conv: 1.027)
{Soda Bichy} -> {Carragal tto} (conf: 0.053, supp: 0.001, lift: 3.714, conv: 1.041)
{Soda Bichy} -> {Toro Blanco tetra} (conf: 0.057, supp: 0.001, lift: 3.222, conv: 1.042)
{Balbo Magnum} -> {Coca 2250cc desc} (conf: 0.059, supp: 0.001, lift: 2.350, conv: 1.036)

{Coca 2l ret} -> {Fernet Branca 3/4} (conf: 0.063, supp: 0.007, lift: 3.142, conv: 1.046)
{Toro Tinto tetra} -> {Colorado 20 Baisha} (conf: 0.066, supp: 0.003, lift: 4.754, conv: 1.056)


{Toro Tinto tetra} -> {Soda Bichy} (conf: 0.073, supp: 0.004, lift: 3.790, conv: 1.058)
{Carragal tto} -> {Richmond} (conf: 0.074, supp: 0.001, lift: 6.714, conv: 1.068)
{Balbo Magnum} -> {Soda Bichy} (conf: 0.076, supp: 0.001, lift: 3.934, conv: 1.061)

{panda} -> {Carragal tto} (conf: 0.077, supp: 0.002, lift: 5.341, conv: 1.068)
{Fanta 2l ret} -> {Quilmes} (conf: 0.091, supp: 0.001, lift: 2.088, conv: 1.052)
{Coca light 2l ret} -> {Sta Florentina Bivarietales} (conf: 0.092, supp: 0.001, lift: 9.262, conv: 1.091)
{Sprite 2l ret y zero 2l ret} -> {Fanta 2l ret} (conf: 0.093, supp: 0.001, lift: 7.064, conv: 1.088)
{Richmond} -> {Carragal tto} (conf: 0.097, supp: 0.001, lift: 6.714, conv: 1.091)
{Hook Cola x 2 1/4 lt} -> {Toro Tinto tetra} (conf: 0.097, supp: 0.001, lift: 2.008, conv: 1.054)
{Gaseosa Talca 2250cc} -> {Carragal tto} (conf: 0.098, supp: 0.002, lift: 6.810, conv: 1.093)
{Coca 2250cc desc} -> {Fernet Branca 1/2 l} (conf: 0.098, supp: 0.002, lift: 8.164, conv: 1.096)
{Fanta 2l ret} -> {Sprite 2l ret y zero 2l ret} (conf: 0.105, supp: 0.001, lift: 7.064, conv: 1.101)

{Carragal tto} -> {panda} (conf: 0.109, supp: 0.002, lift: 5.341, conv: 1.099)
{Carragal tto} -> {Gaseosa Talca 2250cc} (conf: 0.123, supp: 0.002, lift: 6.810, conv: 1.120)
{Rodeo} -> {Toro Tinto tetra} (conf: 0.125, supp: 0.001, lift: 2.579, conv: 1.087)
{Camel 20} -> {Toro Tinto tetra} (conf: 0.138, supp: 0.001, lift: 2.856, conv: 1.104)
{Sprite 2250cc desc} -> {Coca 2250cc desc} (conf: 0.158, supp: 0.001, lift: 6.264, conv: 1.158)

{Richmond} -> {Brahma} (conf: 0.166, supp: 0.002, lift: 2.601, conv: 1.123)
{Colorado 20 Baisha} -> {Toro Tinto tetra} (conf: 0.230, supp: 0.003, lift: 4.754, conv: 1.236)
{Fanta 2l ret} -> {Coca 2l ret} (conf: 0.252, supp: 0.003, lift: 2.148, conv: 1.180)
{Sprite 2l ret y zero 2l ret} -> {Coca 2l ret} (conf: 0.268, supp: 0.004, lift: 2.290, conv: 1.206)
```