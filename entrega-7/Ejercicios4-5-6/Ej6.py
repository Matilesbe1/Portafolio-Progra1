alumnos = {
    1001: "Ana",
    1002: "Bruno",
    1003: "Carla"
}
diccionario_vacio = {}

#a) Mostrar el nombre asociado al legajo 1002 mediante alumnos[1002].
print(alumnos[1002])
#b) Agregar el legajo 1004 y luego modificar el nombre asociado al legajo 1001.
alumnos[1004] = "Lucas"
alumnos[1001] = "Lorenzo" 
#c) Verificar con in si existe el legajo 1010.
if 1010 in alumnos:
    print("Existe")
else:
    print("No existe")
#d) Consultarlo con get() y un mensaje alternativo.
verificar_con_get = alumnos.get(1010, "No se encontro")
print(verificar_con_get)
#e) Intentar acceder directamente a la clave inexistente y capturar KeyError.
try:
    print(alumnos[1010])
except KeyError:
    print("El legajo 1010 no existe")
#f) Eliminar un legajo existente con del, luego de comprobar su existencia.
if 1001 in alumnos:
    del alumnos[1001]
    
print(alumnos)