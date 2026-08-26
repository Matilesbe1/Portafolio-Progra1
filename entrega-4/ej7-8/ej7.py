#7. Tuplas anidadas
'''Resolver: 
a) Mostrar el nombre del segundo alumno. 
b) Mostrar la fecha completa del tercer alumno. 
c) Mostrar únicamente el mes de nacimiento del primer alumno. 
d) Recorrer la estructura y mostrar nombre, día, mes y año con formato legible.'''

alumnos = ( ("Ana", (12, "Marzo", 2005)), ("Bruno", (8, "Julio", 2004)), ("Carla", (21, "Enero", 2005)) )

# Punto A
print(alumnos[1][0]) # Bruno

#Punto B
print(alumnos[2][1]) # (21,"Enero",2005)

#Punto C
print(alumnos[0][1][1]) # Marzo

#Punto D
print(f"{"Nombre":<10}|{"Dia":>5}|{"Mes":>5}|{"Año":>5}|")
for alumno in alumnos:
    print(f"{alumnos}")