productos = ("Teclado", "Mouse", "Monitor", "Auriculares", "Webcam")
# PUNTO A
print(f"Primer elemento: {productos[:1]}")
print(f"Ultimo elemento: {productos[-1:]}")
mitad = len(productos)//2
print(f"Elemento central: {productos[mitad:mitad+1]}")
# PUNTO B
print(productos[:3])
# PUNTO C
print(productos[2:])
# PUNTO D
print(productos[::-1])
# PUNTO E
for i in productos:
    print(f"Productos: {i}")
# PUNTO F
productos[0] = "Notebook"
# Da TypeError ya que las tuplas son inmutables y no las podes cambiar.