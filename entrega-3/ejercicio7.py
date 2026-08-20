"""
Desarrollen un programa que solicite nombre del producto, precio unitario y cantidad. El precio deberá convertirse a float
y la cantidad a int. Luego calculen el importe total.
Muestren el resultado de dos maneras:
a) Utilizando una f-string y formato de dos decimales.
b) Utilizando concatenación; conviertan explícitamente los valores numéricos con str().
Comparen legibilidad, cantidad de conversiones necesarias y resultado obtenido
"""

producto = input("Producto:")
precio = float(input("Precio unitario:"))
cantidad = int(input("Cantidad:"))
total = precio * cantidad

#Mostramos el resultado con f-string
print(f"El producto elegido fue: {producto}, lleva {cantidad} unidad/es, con un precio unitario de: {precio} y su precio total es: {total}")

#Mostramos el resultado con concatenacion
print ("El producto elegido fue: " + producto , "lleva " + str(cantidad) ,"unidades/es, con un precio unitario de: " + str(precio), "y su precio total es: " + str(total))

