"""Crear un diccionario cuya clave sea el nombre de un grupo y cuyo valor sea un conjunto con las tecnologías que utiliza. 
Esta estructura combina dos niveles: el diccionario localiza al grupo y el conjunto evita tecnologías repetidas.

a) Agreguen un nuevo grupo.
b) Incorporen una tecnología a un grupo existente.
c) Consulten un grupo mediante get() sin provocar una excepción.
d) Recorran el diccionario mostrando cada grupo y sus tecnologías ordenadas solo para la presentación
"""
tecnologias_por_grupo = {
 "Grupo 1": {"Python", "Git"},
 "Grupo 2": {"Python", "JSON"}
}

#A) Incorporamos un nuevo grupo
tecnologias_por_grupo["Grupo 3"] = set()

#B) Incoporamos la tecnologia python al grupo 3
tecnologias_por_grupo["Grupo 3"].add("Python")

#C)
print ("\n--- Tecnologias del grupo 1 ---")
print (tecnologias_por_grupo.get("Grupo 1"))

#D)Reccoremos todo el diccionario y mostramos cada grupo con su tecnologia 
print ("\n--- Grupos y sus tecnologias ---")
for grupo,tecnologia in tecnologias_por_grupo.items():
    print (grupo,tecnologia)

