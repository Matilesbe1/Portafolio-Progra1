"""
Resolver:
a) Recorrer directamente el diccionario y mostrar sus claves.
b) Mostrar las cantidades mediante values().
c) Mostrar cada producto y su stock mediante items().
d) Informar la cantidad de productos diferentes con len().
e) Calcular el total de unidades disponibles.
f) Informar el producto con mayor stock mediante max(stock, key=stock.get).
La expresión max(stock.values()) devuelve la mayor cantidad, pero no identifica el producto. Para obtener la clave 
asociada al mayor valor puede utilizarse max(stock, key=stock.get). Analicen qué ocurriría si el diccionario estuviera vacío 
o si dos productos compartieran la cantidad máxima
"""

stock = {
 "teclado": 12,
 "mouse": 20,
 "monitor": 7,
 "webcam": 5
}

print ("\n---- Claves del diccionario ----")
for producto in stock:
    print (producto)

print ("\n---- Cantidades ----")
for cantidad in stock.values():
    print (cantidad)

print ("\n---- Producto y stock ----")
for producto,cantidad in stock.items():
    print (producto,cantidad)

print ("\n---- Cantidad productos diferentes ----")
print (len(stock))

print ("\n---- Unidades disponibles ----")
print ("Total de unidades disponibles", sum(stock.values()))

print("\n---- Producto con mayor stock ----")
producto_mayor = max(stock, key=stock.get)
print (f"EL producto con mayor stock es {producto_mayor} y son {stock[producto_mayor]} unidades")