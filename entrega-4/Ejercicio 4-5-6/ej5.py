ventas = (120, 85, 230, 150, 90, 150)
# PUNTO A
print(f"Cantidad: {len(ventas)}")
print(f"Mayor: {max(ventas)}")
print(f"Menor: {min(ventas)}")
print(f"Suma: {sum(ventas)}")
# PUNTO B
if 150 in ventas:
    print("Pertenencia")
if 500 not in ventas:
    print("Ausencia")
# PUNTO C 
print(f"150 aparece: {ventas.count(150)} veces")
# PUNTO D
print(f"La primer posicion de 230 es: {ventas.index(230)}")
# PUNTO E
ventas += (300, 250)
print(f"Nueva tupla: {ventas}")
# PUNTO F
print((0,1)*3)