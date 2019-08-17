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

## Por productos

```
python3 asociar-productos.py

```