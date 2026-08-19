#4. Rebanas (Slicing) para obtener nuevas listas
juegos = ["Minecraft", "Valorant", "Fortnite", "FIFA", "Rocket League", "Roblox", "LOL", "Among Us"]
print ("-" *50)
print (juegos , "\n")

#a) Los tres primeros elementos.
print ("Los tres primeros elementos:" , juegos[0:3])
#b) Los cuatro últimos elementos.
print("Los cuatro últimos elementos:" , juegos[4:8])
#c) Los elementos ubicados desde la posición 1 hasta la 4 inclusive.
print("Los elementos desde la posición 1 hasta la 4:" , juegos[1:5])
#d) Los elementos de posiciones pares.
print("Los elementos de posiciones pares:" , juegos[::2])
#e) Los elementos de posiciones impares.
print("Los elementos de posiciones impares:" , juegos[1::2])
#f) La lista invertida.
print("La lista invertida:" ,juegos[::-1])
#g) Todos los elementos excepto el primero.
print("Todos los elementos excepto el primero:" , juegos[1:])
#h) Todos los elementos excepto el último.
print("Todos los elementos excepto el último:" , juegos[:-1])

print ("-" *50)

#5 Modificacion de listas mediante slicing
numeros = [2, 4, 6, 8, 10, 12, 14]
print (numeros , "\n")

#a) Reemplazar 6 y 8 por 60 y 80.
numeros[2:4] = [60,80]
print ("remplazamos 6 y 8:" ,numeros)
#b) Eliminar 10 y 12.
numeros[4:6] = []
print ("eliminamos 10 y 12:" ,numeros)
#c) Insertar 100 y 200 entre 4 y 6 utilizando una rebanada nula.
numeros[2:2] = [100,200]
print ("Insertamos entre el 4 y 6:" ,numeros)
#d) Agregar tres valores al comienzo.
numeros[0:0] = [101,102,103]
print ( "Agregramos 3 numeros al comienzo:" , numeros)
#e) Vaciar la lista utilizando una rebanad
numeros [0:] = []
print ("Vaciamos la lista" , numeros)

print ("-" * 50)